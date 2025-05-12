# QuoteHub – Daily Quote Sharing App

QuoteHub is a simple Flask-based web app that shows random inspirational programming quotes.

## 🔧 Stack

- Python + Flask
- HTML + JS
- Docker
- Jenkins
- Git + GitHub

## 🗂️ Branches

- `api` – REST API (`/api/quote`)
- `main` – Frontend integration and UI

## 🐳 Docker Instructions

```bash
docker build -t quotehub .
docker run -d -p 5000:5000 quotehub

