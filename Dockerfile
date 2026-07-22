# Use a lightweight, official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
# (If you don't have a requirements.txt, we will create it below)
COPY requirements.txt .

# Install dependencies without caching the package index to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY app.py .

# Expose the port the Flask app runs on
EXPOSE 5000

# Set standard environment variables
# - Python unbuffered ensures logs print to the terminal instantly
# - Define a default environment variable for testing
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=docker-development

# Run the application
CMD ["python", "app.py"]
