# Python Zaragoza Community website

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Reflex](https://img.shields.io/badge/Reflex-0.3.9-8B5CF6)](https://reflex.dev/)

Official website of the **Python Zaragoza** community built with [Reflex](https://reflex.dev/) and deployed on GitHub Pages.

![PyZgz Logo](assets/logo.png)

## 🚀 About Python Zaragoza

Python Zaragoza is a local community of Python enthusiasts in Zaragoza, Spain. We organize:

- 📅 **Meetups**: Technical talks and networking events
- 🛠️ **Workshops**: Hands-on coding sessions for all skill levels
- 🤝 **Collaborative Projects**: Open-source initiatives and group projects
- 🌟 **Community Events**: Hackathons, sprints, and social gatherings

Our mission is to foster a welcoming and inclusive environment for learning and sharing knowledge about Python and related technologies.

## ✨ Features

- 🌓 Dark/Light mode with system preference detection
- 📱 Fully responsive design
- ⚡ Fast static site generation
- 📅 Event management and display
- ✉️ Contact form functionality
- 📝 Blog section for community updates

## 📂 Project Structure

```
.
├── assets/                  # Static assets (images, icons, generated data)
│   ├── events.json         # Auto-generated events data
│   └── logo.png            # Community logo
├── src/
│   └── pyzgz_site/         # Reflex application code
│       ├── __init__.py
│       ├── pyzgz_site.py   # Main app configuration and routes
│       ├── layout.py       # Shared layout components and styles
│       ├── index_page.py   # Home page
│       ├── events_page.py  # Events listing
│       ├── blog_page.py    # Blog section
│       ├── talks_page.py   # Talk submission
│       ├── about_page.py   # About the community
│       └── contact_page.py # Contact form
├── .github/workflows/      # GitHub Actions workflows
│   └── pages.yml           # GitHub Pages deployment
├── pyproject.toml          # Python project metadata and dependencies
├── uv.lock                 # Locked dependencies (uv)
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Node.js 18+ (for Reflex development server)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PythonZaragoza/python-zaragoza.github.io.git
   cd python-zaragoza.github.io
   ```

2. **Set up the environment and install dependencies:**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Start the development server:**
   ```bash
   uv run reflex run
   ```
   The site will be available at http://localhost:3000

4. **Build for production:**
   ```bash
   uv run reflex export --frontend-only
   ```
   The static files will be generated in `.web/build/client`

## 🌐 Deployment

The site is automatically deployed to GitHub Pages on every push to the `main` branch using GitHub Actions.

### Manual Deployment

1. Build the static site:
   ```bash
   uv run reflex export --frontend-only
   ```

2. The static files will be in `.web/build/client`

3. Configure your GitHub Pages to serve from the `gh-pages` branch or the `docs/` folder

## 🛠️ Development

### Available Scripts

- `uv run reflex run` - Start development server
- `uv run reflex export --frontend-only` - Build static site
- `uv run pytest` - Run tests (when available)

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Format code with [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/)

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

- Website: [python-zaragoza.github.io](https://python-zaragoza.github.io)
- Meetup: [meetup.com/python_zgz](https://www.meetup.com/es-ES/python_zgz/)
- Email: zaragoza@es.python.org

---

## 📬 Contact and Talks

- **Propose a talk (CFP):** send your proposal to `zaragoza@es.python.org`.
  Include title, abstract, approximate duration and level.
- **General contact:** `zaragoza@es.python.org`.

### Talks form (Google Forms)

The `Charlas` page links to a **Google Form**:

- Current link: `https://forms.gle/qvMCiq8GkyCty79N8` (configurable in `pyzgz/talks_page.py`, constant `GOOGLE_FORM_URL`).
- Alternatively, email us at `zaragoza@es.python.org`.

---

## ⚙️ Configuration

For static deployment on GitHub Pages **no environment variables are required**.
If backend/APIs get integrated in the future, they will be documented here.

### Meetup events

- **Group**: `python_zgz`.
- **Without token**: the build uses the public iCal feed and generates `assets/events.json` with upcoming events only.
- **With token (optional)**: add a `MEETUP_TOKEN` secret in the repo so the workflow also fetches past events via the API.
- **Workflow**: `.github/workflows/pages.yml` runs `scripts/fetch_meetup.py` before `reflex export`.
- **Local test**:
  ```bash
  # Generate events.json (without token uses iCal)
  uv run python scripts/fetch_meetup.py
  # Run the site
  uvx reflex run
  ```

---

## 📜 License

[MIT](LICENSE)

---

## 🗺️ Roadmap

- [x] **Initial pages structure**: home, community, about, contact, blog, events, talks (CFP).
- [ ] **Persistent status messages**: better UX when navigating between pages.
- [ ] **Fetch Meetups**:
  - Server: consume API with `MEETUP_TOKEN`.
  - Static: prebuild `assets/events.json` in GitHub Actions.
- [ ] **SEO & accessibility**: meta tags, OpenGraph, manifest, favicon.
- [ ] **Visual design improvements**: light/dark theme, custom styles.
- [x] **Automated deployment** on GitHub Pages with a stable workflow.
- [ ] **Optional** English/Spanish i18n.

---

**Made with ❤️ in Zaragoza.**

---

## 🤝 Contributing

- **Dev dependencies** are declared under the `dev` group in `pyproject.toml` (ruff, black, pre-commit, pytest).
- **Setup**:
  ```bash
  uv sync --group dev
  uv run pre-commit install
  ```
- **Run linters/formatters manually**:
  ```bash
  uv run ruff check --fix .
  uv run ruff format .
  uv run black .
  ```
- **Run hooks on all files**:
  ```bash
  uv run pre-commit run --all-files
  ```
- **Tests** (placeholder):
  ```bash
  uv run pytest -q
  ```
