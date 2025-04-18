# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (adjust if your app runs on a different port)
EXPOSE 8080

# Run the app (update this if your app entry point is different)
CMD ["python", "app.py"]
