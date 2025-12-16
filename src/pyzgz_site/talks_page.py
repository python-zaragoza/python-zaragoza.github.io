import reflex as rx

from pyzgz_site.layout import EMAIL, page_wrapper, styles

GOOGLE_FORM_URL = "https://forms.gle/qvMCiq8GkyCty79N8"


def talks():
    """Talk proposal via Google Forms (with optional email alternative)."""
    return page_wrapper(
        rx.section(
            rx.vstack(
                rx.heading("Propón una charla"),
                rx.text("Envíanos tu propuesta a través de nuestro formulario:"),
                rx.link(
                    rx.button("Abrir formulario de Charlas", variant="solid"),
                    href=GOOGLE_FORM_URL,
                    is_external=True,
                ),
                rx.text("Como alternativa, puedes escribirnos a:"),
                rx.link(EMAIL, href=f"mailto:{EMAIL}", is_external=True),
                spacing="4",
                align="center",
            ),
            style=styles["section"],
        ),
    )
