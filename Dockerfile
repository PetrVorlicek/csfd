FROM ghcr.io/astral-sh/uv:python3.14-rc-bookworm-slim

# Create user 
RUN groupadd -r appgroup && \
    useradd --no-log-init -r -g appgroup -d /home/appuser -m appuser

# Copy files
WORKDIR /home/appuser/app
RUN chown -R appuser:appgroup /home/appuser/app
COPY --chown=appuser:appgroup . .

# Install dependencies
USER appuser
RUN uv sync --locked
RUN uv venv

# Run the app
WORKDIR /home/appuser/app/mediaboard_task
EXPOSE 8000
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]