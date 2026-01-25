# Profile REST API

Source code for the Profile REST API course projects.

A simple, extensible REST API for managing user profiles (name, email, bio, etc.). This repository contains example implementations, tests, and deployment instructions so you can run the service locally, run tests, and package it in Docker.

> NOTE: This README is intentionally implementation-agnostic. If your project uses a particular framework (FastAPI, Flask, Django REST Framework, etc.), follow the matching sections below or adapt commands to your code structure.

## Table of contents

- [Features](#features)
- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Environment variables](#environment-variables)
  - [Run (development)](#run-development)
- [API endpoints](#api-endpoints)
- [Examples](#examples)
- [Testing](#testing)
- [Docker](#docker)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- CRUD operations for profiles
- JSON input/output
- Validation and basic error handling
- Tests (unit/integration) with pytest
- Dockerfile included (optional)
- Example environment configuration

## Tech stack

- Language: Python (100%)
- Test runner: pytest (recommended)
- Web frameworks: FastAPI or Flask (examples provided)
- Optional: SQLAlchemy or an ORM of your choice, or simple in-memory store for examples

## Getting started

### Requirements

- Python 3.8+
- pip
- git
- (Optional) Docker

### Install

1. Clone the repository:
   ```bash
   git clone https://github.com/Skull1zues/profile-rest-api.git
   cd profile-rest-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows (PowerShell)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

If this repo doesn't include a `requirements.txt`, install your framework and test libs manually, for example:
```bash
pip install fastapi uvicorn[standard] pydantic sqlalchemy alembic pytest
# or for Flask:
pip install flask flask-restful pytest
```

### Environment variables

Create a `.env` file or export environment variables expected by the app. Common variables:

- PORT (default: 8000)
- DATABASE_URL (e.g. sqlite:///./dev.db or PostgreSQL URL)
- SECRET_KEY (if your app signs tokens or sessions)
- LOG_LEVEL (e.g. info, debug)

Example `.env`:
```env
PORT=8000
DATABASE_URL=sqlite:///./dev.db
SECRET_KEY=change-me
LOG_LEVEL=debug
```

### Run (development)

If using FastAPI (recommended for new Python REST APIs):
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port ${PORT:-8000}
```

If using Flask:
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=${PORT:-5000}
```

Adjust paths (`app.main:app`, `FLASK_APP`) to match your project structure.

## API endpoints (example)

These are common endpoints for a profile service. Adjust according to your implementation.

- GET /profiles — list all profiles

