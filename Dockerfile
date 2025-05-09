FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Create virtual environment
RUN python3 -m venv mltbenv

# Install requirements using the virtual environment
COPY requirements.txt .
RUN mltbenv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the Flask port for web traffic
EXPOSE 8080

# Run the bot and Flask server together
CMD ["mltbenv/bin/python3", "main.py"]
