# Product Catalog

Simple Django + DRF app for a take-home assignment: products with categories and tags, a search/filter API, and a minimal HTML page that uses it. Use any of the options below to launch the project

**Stack:** Python 3.13, Django 5.2, DRF, PostgreSQL 17, Docker, uv

## Run with Docker (easiest)

```bash
docker compose up --build -d
```

Then load sample data and create an admin user:

```bash
docker compose exec web python manage.py loaddata sample_data
docker compose exec web python manage.py createsuperuser
```

Open http://localhost:8000 (search page) and http://localhost:8000/admin.

## Run with uv (supposes that you have installed uv)

Needs Docker only for the database.

```bash
docker compose up db -d
uv sync
uv run manage.py migrate
uv run manage.py loaddata sample_data
uv run manage.py createsuperuser
uv run manage.py runserver
```

## Run with pip

Same as above, but with a manual virtualenv:

```bash
docker compose up db -d
python3.13 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_data
python manage.py createsuperuser
python manage.py runserver
```

## API

- `GET /api/products/` — list products
  - `?q=...` — search in name and description
  - `?category=<id>` — filter by category
  - `?tag=<id>&tag=<id>` — filter by tags (any of them)
  - all parameters combine
- `GET /api/categories/`, `GET /api/tags/`

## Notes

- DB credentials in the repo are local dev values, not secrets.
- PostgreSQL was used as it's more close to stack.
- Search matches product name as well as description — assumed intended UX.
- Multiple tags filter with OR ("any of"). `requirements.txt` is generated from `uv.lock`.
- Sample data was entered through the Django admin and was taken from Wilderries, then exported with `dumpdata` to `products/fixtures/sample_data.json`.

## AI usage

2 things has been done using AI: generating base of this README.md and index.html, that contains some regular HTML, CSS and JS logic. README.md has been manually edited and added more details on project. index.html has been reviewed too: mostly deleted redundant code
