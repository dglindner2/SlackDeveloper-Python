from dotenv import load_dotenv
import os
import time
from slack_sdk import WebClient
from slack_bolt import App
from datetime import datetime

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Listening for the 'mybirthday' block/date field
@app.action('mybirthday')
def handle_birthday_selection(body, ack, respond):
    ack()
    selected_date = datetime.strptime(body['actions'][0]['selected_date'], '%Y-%m-%d').date()
    current_date = datetime.now().date()
    day_age = (current_date - selected_date).days
    print('Birthday Received:', selected_date.strftime('%Y-%m-%d'))
    respond_text = f"Wow, cool ... you're {day_age} days old!"
    respond({
        'text': respond_text,
        'delete_original': True
    })


@app.event('app_home_opened')
def request_birthday():
    print('Begin birthday post to channel creator in: ' + os.environ.get('SLACK_BIRTHDAYS_CHANNEL'))
    try:
        channel_result = app.client.conversations_info(
            token=os.environ.get('SLACK_USER_TOKEN'),
            channel=os.environ.get('SLACK_BIRTHDAYS_CHANNEL')
        )
        channel_creator = channel_result['channel']['creator']

        try:
            app.client.chat_postEphemeral(
                token=os.environ.get('SLACK_USER_TOKEN'),
                channel=os.environ.get('SLACK_BIRTHDAYS_CHANNEL'),
                user=channel_creator,
                text="Hello World",
                blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "When is your birthday, channel creator?"
                        },
                        "accessory": {
                            "type": "datepicker",
                            "action_id": "mybirthday",
                            "initial_date": "1999-12-31",
                            "confirm": {
                                "title": {
                                    "type": "plain_text",
                                    "text": "Are you sure this is your birthday?"
                                },
                                "confirm": {
                                    "type": "plain_text",
                                    "text": "Yep!"
                                },
                                "deny": {
                                    "type": "plain_text",
                                    "text": "Sorry, my bad!"
                                }
                            },
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a date"
                            }
                        }
                    }
                ]
            )
        except Exception as post_message_failure:
            print(f"Error posting message: {post_message_failure}")
    except Exception as channel_info_error:
        print(f"Channel error: {channel_info_error}")

# Start your app
if __name__ == "__main__":
    try:
        print("Trying to start this thing...")
        app.start(port=int(os.environ.get('PORT', 3000)))
        print('⚡️ Hello World.. bolt app is running!')
    except Exception as e:
        print(f'Error starting the app: {e}')
