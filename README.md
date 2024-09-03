
## Run Locally

Install dependencies

Make sure you have poetry installed https://python-poetry.org/docs/.

And create PostgreSQL database "crossword".

Go to project directory

And install poetry dependencies:
```bash
poetry install
```

Copy .env.example to .env and edit it:
```bash
cp .env.example .env
```

Run migrations
```bash
alembic upgrade head
```

Start the uvicron server:
```bash
uvicorn app:create_app --factory --reload --port 5000
```
