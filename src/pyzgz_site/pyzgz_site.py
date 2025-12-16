import reflex as rx

from pyzgz_site.about_page import about as about_page
from pyzgz_site.blog_page import blog as blog_page
from pyzgz_site.contact_page import contact as contact_page
from pyzgz_site.events_page import events as events_page
from pyzgz_site.index_page import index as index_page
from pyzgz_site.talks_page import talks as talks_page

# ---------- App & routes ----------
# Configure app for static export
app = rx.App(
    theme=rx.theme(appearance="light"),
)
app.add_page(index_page, route="/", title="PythonZgz — Comunidad Python Zaragoza")
app.add_page(events_page, route="/events", title="Eventos · PythonZgz")
app.add_page(blog_page, route="/blog", title="Blog · PythonZgz")
# app.add_page(comunity_page, route="/comunity", title="Comunidad · PythonZgz")
app.add_page(talks_page, route="/talks", title="Proponer charla · PythonZgz")
app.add_page(about_page, route="/about", title="Sobre · PythonZgz")
app.add_page(contact_page, route="/contact", title="Contacto · PythonZgz")
