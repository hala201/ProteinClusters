FROM python:3.12.8-slim

# Set working directory
WORKDIR /app

# Install system dependencies for DVC, builds, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install DVC with S3 remote support
RUN pip install 'dvc[s3]'

# Copy full project into the container
COPY . .

ENV PYTHONPATH=/app/src

# Default command (runs pipeline)
CMD ["dvc", "repro"]
