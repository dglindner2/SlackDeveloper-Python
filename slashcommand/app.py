import os
import requests
from slack_bolt import App
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    signing_secret=os.environ.get('SLACK_SIGNING_SECRET')
)

# Define an event handler for the "/survey-dgl" command
@app.command("/survey-dgl")
def handle_survey_command(ack, command, payload, context, respond):
    
    # Acknowledge command request
    ack()

    if command["text"] == "":
        respond({"text": "Oops, you didn't provide a sub-command to your Slash command."})
    else:
        # Open a modal powered by Block Kit
        client = WebClient(token=context["bot_token"])
        response_url = command["response_url"]
        client.views_open(
            token = context["bot_token"],
            trigger_id = payload["trigger_id"],
            view = {
                "private_metadata": response_url,
                "type": 'modal',
                "callback_id": 'survey',
                "title": {
                    "type": 'plain_text',
                    "text": f"Survey: {command['text']}",
                "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
                },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": ":wave: Hello!\n\nWe'd love to hear from you how we can make this place the best place you’ve ever worked.",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "block_id": "enjoy_working",
                "type": "input",
                "label": {
                    "type": "plain_text",
                    "text": "You enjoy working here at Acme & Co",
                    "emoji": True
                },
                "element": {
                    "action_id": "enjoy_working_action",
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": [
                        {
                        "text": {
                            "type": "plain_text",
                            "text": "Strongly Agree",
                            "emoji": True
                        },
                        "value": "strongly-agree"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Agree",
                            "emoji": True
                        },
                        "value": "agree"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Neither agree nor disagree",
                            "emoji": True
                        },
                        "value": "neither-agree-nor-disagree"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Disagree",
                            "emoji": True
                        },
                        "value": "disagree"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Strongly disagree",
                            "emoji": True
                        },
                        "value": "strongly-disagree"
                    }
              ]
            }
          },
                              {
                        "block_id": "lunch",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "What do you want for our team weekly lunch?",
                            "emoji": True
                        },
                        "element": {
                            "action_id": "lunch_action",
                            "type": "multi_static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select your favorites",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":pizza: Pizza",
                                        "emoji": True
                                    },
                                    "value": "pizza"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":fried_shrimp: Thai food",
                                        "emoji": True
                                    },
                                    "value": "thai-food"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":desert_island: Hawaiian",
                                        "emoji": True
                                    },
                                    "value": "hawaiian"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":meat_on_bone: Texas BBQ",
                                        "emoji": True
                                    },
                                    "value": "texas-bbq"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":hamburger: Burger",
                                        "emoji": True
                                    },
                                    "value": "burger"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":taco: Tacos",
                                        "emoji": True
                                    },
                                    "value": "tacos"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":green_salad: Salad",
                                        "emoji": True
                                    },
                                    "value": "salad"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": ":stew: Indian",
                                        "emoji": True
                                    },
                                    "value": "indian"
                                }
                            ]
                        }
                    },
                    {
                        "block_id": "anything_else",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Anything else you want to tell us?",
                            "emoji": True
                        },
                        "element": {
                            "action_id": "anything_else_action",
                            "type": "plain_text_input",
                            "multiline": True
                        },
                        "optional": False
                    }
                ]
            }
        )
        
# Define an event handler for the "view_submission" event
@app.view("survey")
def handle_survey_submission(ack, body, view, context):
    # Acknowledge the view_submission event
    ack()

    # Process input
    user_responses_raw = view["state"]["values"]

    user_responses = {
        "enjoy_working": user_responses_raw["enjoy_working"]["enjoy_working_action"]["selected_option"]["value"],
        "lunch": [c["text"]["text"] for c in user_responses_raw["lunch"]["lunch_action"]["selected_options"]],
        "anything_else": user_responses_raw["anything_else"]["anything_else_action"]["value"]
    }
    print("=== User responses ===")
    print(user_responses)

    # Send a message back to the conversation
    response_url = view["private_metadata"]
    message = f":wave: Thank you for completing the survey!\n\nHere are your responses:\n\n- You enjoy working here at Acme & Co: {user_responses['enjoy_working']}\n- Your preferences for the team weekly lunch: {', '.join(user_responses['lunch'])}\n- Additional comments: {user_responses['anything_else']}"
    payload = {
    "text": message
    }

    try:
        response = requests.post(response_url, json=payload)
        print(f"Message sent: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

# Start the app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

