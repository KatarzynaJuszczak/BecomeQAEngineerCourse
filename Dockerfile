# Use an official Python runtime
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the local requirements.txt file to the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container at /app
COPY . .

# Run below command when the container launches
CMD ["pytest", "-k", "test_search_for_existing_repo"]
