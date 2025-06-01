# Mediaboard

A Django application for media management.

## Prerequisites

- Docker
- Python 3.14 (Install UV)

## Setup

### Install uv (Python package manager)

```bash
make install-uv
```

## Development

### Run the development server

```bash
make dev
```

### Run tests

```bash
make test
```

### Run with Docker

```bash
make docker
```

## Available Commands

- `make install-uv` - Install the uv package manager
- `make test` - Run the test suite using pytest
- `make dev` - Start the Django development server
- `make docker` - Build and run the application using Docker Compose
