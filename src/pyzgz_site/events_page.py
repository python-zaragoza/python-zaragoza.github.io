import json
from datetime import UTC, datetime
from pathlib import Path

import reflex as rx

from pyzgz_site.layout import page_wrapper, styles

# Resolve assets/events.json relative to the project root (one level up from this file's dir)
BASE_DIR = Path(__file__).parent.parent.parent
ASSETS_EVENTS = Path(BASE_DIR) / "assets" / "events.json"


def _load_events() -> list[dict]:
    """Static loading of events from assets/events.json.
    Events are loaded during build time, not at runtime.
    """
    # This file is generated during deployment by GitHub Actions workflow
    # See .github/workflows/pages.yml -> fetch_meetup.py
    try:
        # Try to load events from the generated file
        if not Path(ASSETS_EVENTS).exists():
            return [
                {
                    "name": "No hay eventos próximamente",
                    "description": "Vuelve pronto para ver nuestros próximos eventos",
                },
            ]

        with Path(ASSETS_EVENTS).open(encoding="utf-8") as f:
            data = json.load(f)

        # Ensure we always return a list
        if not isinstance(data, list):
            return [
                {
                    "name": "Error cargando eventos",
                    "description": "Disculpa, hubo un problema al cargar los eventos",
                },
            ]

        return data

    except Exception as e:
        print(f"Error cargando eventos: {e}")
        return [
            {
                "name": "Error cargando eventos",
                "description": "Disculpa, hubo un problema al cargar los eventos",
            },
        ]


def _parse_when(ev: dict) -> datetime | None:
    """Parse event date from common fields (iso string or epoch ms)."""
    # Accept 'time' (ms since epoch) or 'date'/'local_date' (ISO-like)
    t = ev.get("time")
    if isinstance(t, (int, float)):
        try:
            return datetime.fromtimestamp(float(t) / 1000.0, tz=UTC)
        except Exception:
            pass
    for key in ("date", "local_date", "utc_time", "iso_time"):
        val = ev.get(key)
        if isinstance(val, str):
            try:
                # Try full ISO first
                return datetime.fromisoformat(val.replace("Z", "+00:00"))
            except Exception:
                try:
                    # Try date only
                    return datetime.strptime(val, "%Y-%m-%d").replace(
                        tzinfo=UTC,
                    )
                except Exception:
                    pass
    return None


def _format_when(dt: datetime | None) -> str:
    if not dt:
        return ""
    local = dt.astimezone()  # viewer local time
    return local.strftime("%d %b %Y, %H:%M")


def _split_events(events: list[dict]) -> tuple[list[dict], list[dict]]:
    now = datetime.now(UTC)
    enriched: list[tuple[dict, datetime | None]] = [(e, _parse_when(e)) for e in events]
    upcoming = [e for e, d in enriched if d and d >= now]
    past = [e for e, d in enriched if d and d < now]
    # sort
    upcoming.sort(key=lambda e: _parse_when(e) or now)
    past.sort(key=lambda e: _parse_when(e) or now, reverse=True)
    return upcoming, past


def _event_card(ev: dict) -> rx.Component:
    title = ev.get("name") or ev.get("title") or "Evento"
    url = ev.get("link") or ev.get("url") or "#"
    when = _format_when(_parse_when(ev))
    venue = ev.get("venue", {}).get("name") if isinstance(ev.get("venue"), dict) else ev.get("venue")
    # desc = ev.get("description") or ev.get("short_description") or ""
    return rx.card(
        rx.vstack(
            rx.link(title, href=url, is_external=True, font_weight="bold"),
            rx.text(when, color="gray"),
            rx.cond(venue is not None, rx.text(str(venue))),
            # rx.cond(bool(desc), rx.text(str(desc)) ),
            spacing="2",
            align="start",
        ),
        width="100%",
        align="center",
    )


def events():
    data = _load_events()
    if not data:
        # Fallback view when there's no data yet
        return page_wrapper(
            rx.section(
                rx.vstack(
                    rx.heading("Eventos"),
                    rx.text(
                        "Aún no hay eventos cargados. Pronto mostraremos los próximos y pasados desde Meetup.",
                        text_align="center",
                    ),
                    rx.link(
                        "Ir a nuestro Meetup →",
                        href="https://www.meetup.com/es-ES/python_zgz/",
                        is_external=True,
                    ),
                    spacing="3",
                    align="center",
                ),
                style=styles["section"],
            ),
        )

    upcoming, past = _split_events(data)

    return page_wrapper(
        rx.section(
            rx.vstack(
                rx.heading("Eventos"),
                rx.cond(
                    len(upcoming) > 0,
                    rx.vstack(
                        rx.heading("Próximos", size="5"),
                        rx.grid(
                            *[_event_card(ev) for ev in upcoming],
                            columns={"base": "1", "md": "2"},
                            gap="4",
                            width="100%",
                            justify="center",
                        ),
                        spacing="3",
                        width="100%",
                        align="center",
                    ),
                ),
                rx.cond(
                    len(past) > 0,
                    rx.vstack(
                        rx.heading("Pasados", size="5"),
                        rx.grid(
                            *[_event_card(ev) for ev in past],
                            columns={"base": "1", "md": "2"},
                            gap="4",
                            width="100%",
                            justify="center",
                        ),
                        spacing="3",
                        width="100%",
                        align="center",
                    ),
                ),
                rx.link(
                    "Ver más en Meetup →",
                    href="https://www.meetup.com/es-ES/python_zgz/",
                    is_external=True,
                ),
                spacing="5",
                align="center",
                width="100%",
            ),
            style=styles["section"],
        ),
    )
