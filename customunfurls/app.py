import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_bolt import App 

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Custom unfurls
@app.event('link_shared')
def link_shared_event(event, context):
    print('got a link share event')
    unfurls = {}
    for link in event['links']:
        unfurl_blocks = [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': 'This is a custom unfurl, made possible by calling the Slack `chat.unfurl` API'
                }
            },
            {
                'type': 'divider'
            },
            {
                'type': 'section',
                'fields': [
                    {
                        'type': 'mrkdwn',
                        'text': f'*Domain:*\n{link["domain"]}'
                    },
                    {
                        'type': 'mrkdwn',
                        'text': f'*URL:*\n{link["url"]}'
                    }
                ]
            },
            {
                'type': 'divider'
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': 'Was this unfurl helpful?'
                }
            },
            {
                'type': 'actions',
                'elements': [
                    {
                        'type': 'button',
                        'text': {
                            'type': 'plain_text',
                            'emoji': True,
                            'text': 'Yes :100: '
                        },
                        'style': 'primary',
                        'value': 'yes_helpful'
                    },
                    {
                        'type': 'button',
                        'text': {
                            'type': 'plain_text',
                            'emoji': True,
                            'text': 'Needs work :thumbsdown:'
                        },
                        'style': 'danger',
                        'value': 'no_needs_work'
                    }
                ]
            }
        ]
        unfurls[link['url']] = {'blocks': unfurl_blocks}

    client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
    client.chat_unfurl(
        channel=event['channel'],
        ts=event['message_ts'],
        unfurls=unfurls
    )

# Start your app
if __name__ == "__main__":
    try:
        app.start(port=int(os.environ.get('PORT', 3000)))
        print('⚡️Hello World.. Bolt app is running!')
    except Exception as e:
        print(f'Error starting the app: {e}')


