# Use the official Python image
FROM python:3.12.6

# Set the working directory in the container
WORKDIR /app

# Install SQLite
#RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Copy the requirements file first (for caching purposes)
COPY requirements.txt /app/

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the app directory in your local project
COPY app/ /app/

# Make the wait-mysql.sh script executable
RUN chmod +x wait-mysql.sh

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]