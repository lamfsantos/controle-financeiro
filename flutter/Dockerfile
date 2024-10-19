# Base image
FROM cirrusci/flutter:3.7.7

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the working directory
COPY app/ /app/

# Create a non-root user
RUN useradd -ms /bin/bash flutteruser

# Change ownership of the Flutter SDK and the app directory
RUN chown -R flutteruser:flutteruser /sdks/flutter /app

# Switch to the non-root user
USER flutteruser

# Add the Flutter SDK to safe directories for git
RUN git config --global --add safe.directory /sdks/flutter

# Create the Flutter project (add web support)
RUN flutter create .

# Run pub get to install dependencies
RUN flutter pub get

# Expose the port the Flutter app will run on
EXPOSE 8000

# Command to start the Flutter web server
CMD ["flutter", "run", "-d", "web-server", "--web-port", "8000", "--web-hostname", "0.0.0.0"]

