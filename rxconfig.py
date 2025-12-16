"""Reflex config."""

import reflex as rx

config = rx.Config(
    app_name="pyzgz_site",
    frontend_port=0,
    backend_port=0,
    plugins=[
        rx.plugins.SitemapPlugin(),
    ],
)
