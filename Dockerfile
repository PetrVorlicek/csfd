FROM ghcr.io/astral-sh/uv:python3.14-rc-bookworm-slim AS base

# Create a non-root user and group
RUN groupadd -r appgroup && \
    useradd --no-log-init -r -g appgroup -d /home/appuser -m appuser

# Set the working directory in the container
WORKDIR /home/appuser/app

# Copy the requirements file into the container
# Ensure the appuser owns this file
COPY --chown=appuser:appgroup requirements.txt .

# Install any needed packages specified in requirements.txt using uv
# --system flag installs packages into the global Python environment of the container
RUN uv pip install --no-cache-dir -r requirements.txt --system

# Copy the rest of the application's code into the container
# Ensure the appuser owns these files
COPY --chown=appuser:appgroup . .

# Switch to the non-root user
USER appuser

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the application
# Using Django's development server. For production, consider Gunicorn or Uvicorn.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]