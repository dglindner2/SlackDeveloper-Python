import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# A slash command that shows an ephemeral message
@app.command('/weather-dgl')
def weather_command(ack, command, context):
    ack()
    try:
        client = WebClient(token=context['bot_token'])
        client.chat_postEphemeral(
            channel=command['channel_id'],
            user=command['user_id'],
            text='Hello World',
            blocks=[
                {
                    'type': 'section',
                    'block_id': 'block1',
                    'text': {
                        'type': 'mrkdwn',
                        'text': 'Which city would you like a weather report for? :sunny::snowman_without_snow::umbrella:'
                    },
                    'accessory': {
                        'type': 'external_select',
                        'placeholder': {
                            'type': 'plain_text',
                            'text': 'Select an item'
                        },
                        'action_id': 'choose_city',
                        'min_query_length': 3
                    }
                }
            ]
        )
    except SlackApiError as e:
        print(f"Failed to post ephemeral message: {e.response['error']}")

# Responds with options
@app.options('choose_city')
def choose_city_options(ack):
    results = [
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'London', 'value': 'LON'},
        {'label': 'San Francisco', 'value': 'SF'}
    ]

    options = [
        {
            'text': {
                'type': 'plain_text',
                'text': result['label']
            },
            'value': result['value']
        }
        for result in results
    ]
    
    ack(options=options)

# Prompt weather condition based on selection
@app.action('choose_city')
def choose_city_action(ack, say, action):
    ack()
    selected_city = action['selected_option']['value']
    if selected_city == 'NYC':
        say(f"You selected the option {action['selected_option']['text']['text']} --> It's 80 degrees right now in New York!")
    elif selected_city == 'LON':
        say(f"You selected the option {action['selected_option']['text']['text']} --> It's 60 degrees right now in London!")
    elif selected_city == 'SF':
        say(f"You selected the option {action['selected_option']['text']['text']} --> It's 70 degrees right now in San Francisco!")


# Start your app
if __name__ == "__main__":
    try:
        app.start(port=int(os.environ.get('PORT', 3000)))
        print('⚡️Hello World.. Bolt app is running!')
    except Exception as e:
        print(f'Error starting the app: {e}')
