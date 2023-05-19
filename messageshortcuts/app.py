from dotenv import load_dotenv
import os
from slack_sdk import WebClient
from slack_bolt import App

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Waiting for the save4later message action to be called, which will retrieve a message link
# and post it to the user who initiated the action in their app home
@app.shortcut('save4later-dgl')
def save4later_shortcut(ack, shortcut, say, respond, context):
    ack()

    try:
        result_link = app.client.chat_getPermalink(
            token=context['bot_token'],
            channel=shortcut['channel']['id'],
            message_ts=shortcut['message_ts']
        )

        the_message = f":wave: Hi there! Remember when you thought you'd enjoy this interesting message {result_link['permalink']}? Thank yourself for this!"

        try:
            app.client.chat_postMessage(
                token=context['bot_token'],
                channel=shortcut['user']['id'],
                as_user=True,
                text=the_message
            )
            print(f"Remember request sent to {shortcut['user']['id']}")
        except Exception as post_message_failure:
            print(f"Error posting message: {post_message_failure}")
    except Exception as permalink_failure:
        print(f"Error retrieving permalink: {permalink_failure}")

if __name__ == "__main__":
    try:
        app.start(port=int(os.environ.get('PORT', 3000)))
        print('⚡️ Bolt app is running!')
    except Exception as e:
        print(f'Error starting the app: {e}')