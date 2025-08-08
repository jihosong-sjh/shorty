# Stage 1: Builder - Install dependencies
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runner - Final image
FROM python:3.11-slim-bullseye AS runner

WORKDIR /app

# Copy the virtual environment from the builder
COPY --from=builder /opt/venv /opt/venv

# Copy the application code
COPY ./app ./app

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port and run the application
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
