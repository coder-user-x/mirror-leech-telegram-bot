from threading import Thread
from flask import Flask
import bot  # assuming this is where your bot's main code is

# Dummy web server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
    import bot  # This should start the bot

if __name__ == "__main__":
    # Run Flask in a separate thread
    Thread(target=run_flask).start()

    # Run the bot
    run_bot()
