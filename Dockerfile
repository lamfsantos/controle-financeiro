# Use the official Python image
FROM python:3.12.6

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first (for caching purposes)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the app directory in your local project
COPY app/ /app/

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]