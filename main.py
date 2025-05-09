from threading import Thread
from flask import Flask
import bot  # your existing bot module

# Dummy web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    import bot  # Make sure this runs the bot loop

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
