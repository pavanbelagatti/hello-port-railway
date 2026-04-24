# hello-port-railway

Tiny Flask app scaffolded by the **DevOps Platform Agent** in [Port](https://port.io) and deployed to [Railway](https://railway.app).

## Stack

- Python 3.11
- Flask 3.0
- Gunicorn (production server)

## Endpoints

- `GET /` → renders a landing page
- `GET /health` → JSON health check

## Deployment

Railway auto-detects Procfile and deploys on every push to `main`.

## Scaffolded via

```
Port → DevOps Platform Agent → push_file_to_github action → GitHub API
```
