# Use a Python image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the Flask project files to the container
COPY . /app

# Copy the Scores.txt file to the container
COPY Scores.txt /Scores.txt

# Install the Python dependencies
RUN pip install Flask

# Set the environment variable to specify the Flask app
ENV FLASK_APP=MainScores.py

# Expose the port the Flask app runs on
EXPOSE 5000

# Set the Flask app to run as the default command
CMD ["flask", "run", "--host=0.0.0.0"]
