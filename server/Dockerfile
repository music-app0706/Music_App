FROM python:3.14-slim

# Don't create .pyc files, show logs right away, and keep pip from saving
# extra files. This keeps the image small and the logs readable.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Copy the code in and install it, along with everything it needs.
COPY pyproject.toml ./
COPY app ./app
RUN pip install .

# Run the app as a normal user instead of the admin (root) user, for safety.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# Every 10 seconds, Docker visits /health to check that the app is still up.
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=2)"

# Start the API.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
