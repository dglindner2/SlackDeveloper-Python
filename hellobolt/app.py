import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Define an event handler for the "app_mention" event
@app.event("app_mention")
def handle_mention(body, say, logger):
    logger.info(body)
    say("Hello, I received a mention!")

@app.event("app_home_opened")
def handle_app_home_opened_events(event, say, logger):
    user = event["user"]
    say(f"Hello world and <@{user}>! Great job completing lab 1!")

# Start your app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.start(port=port)
    print(f"⚡️ Hello World.. Bolt is running on port {port}!")
