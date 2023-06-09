# SlackDeveloper-Python
Workshop 7 of the Slack Developer Course

#### Set up your practice environment

`$ mkdir hellobolt`

`$ cd hellobolt`

`$ touch .env`

`$ pip3.11 install slack-sdk`

`$ pip3.11 install python-dotenv`

Start ngrok in its own tab on your local machine

`$ ngrok http 3000`

Run the code in the *hellobolt/app.py* script

`$ python3.11 app.py`

### Exercise 1. Hello World

Subscribe to the following bot events:
- **app_home_opened**

Add the following listener to the *hellobolt/app.py* script:

```
@app.event("app_home_opened")
def handle_app_home_opened_events(event, say, logger):
    user = event["user"]
    say(f"Hello world and <@{user}>! Great job completing lab 1!")
```

### Exercise 2. Events API

Go to App Home section in sidebar. Scroll down to the Show Tabs section and then look below Messages Tab. Select the checkbox for Allow users to send Slash commands and messages from the messages tab.

Subscribe to the following bot events

- **message.im**
- **message.mpim**
- **message.groups**
- **message.channels**

Add the following listener to the *eventsapi/app.py* script:

```
@app.message("hello")
def handle_hello_message(message, say, logger):
    user = message["user"]
    say(f"Hey there <@{user}>! You're done with lab two!")
```

If it isn't working for you, try restarting the Slack application on your machine altogether to make sure the latest updates are included (enabling messaging with the App).

### Exercise 3. Slash Commands

Go to app page, select **Slash Commands** and then select **Create New Command**.

Enter a command called *'/survey-dgl'* and provide a short description.

Enter your Request URL from ngrok.

Click **Save** and reinstall your app as prompted.

From your app page, select **Interactivity & Shortcuts.**

Turn on Interactivity and add the Request URL from ngrok.

Run the *'slashcommands/app.py'* script.

In a channel in the workspace type: `/survey-dgl lunch`.

### Exercise 4. Message Menus

Select **Interactivity & Shortcuts**. 

Copy/Paste Request URL under Interactivity to the **Options Load URL** box under **Select Menus**

Save changes.

Run the script *'messagemenus/app.py'*. 

Keep in mind that you must do this in a channel the app belongs to or in a DM with the application or this will not work.

### Exercise 5. Custom Unfurls

Go to **OAuth & Permissions** page and add `links:read` and `links:write` under **Bot Token Scopes**.

Go to **Event Subscriptions**. 

Under **Subscribe to Bot Events**, subscribe to the `link_shared` event.

In the **App Unfurl Domains** section select **Add Domain.**

Enter the example domain, 'xyz.example.com', and press **Done**.

Press **Save Changes** and then reinstall your application.

Run the script *'customunfurls/app.py'*.

Post `https://xyz.example.com` in a DM to the App. You should see an unfurled URL returned.

### Exercise 6. Message Shortcuts

Message Shortcuts allow users to invoke your app from Slack messages by selecting the … button. Message shortcuts allow you to take action on a specific message. This is different from slash commands, which are only aware of the channel that the slash command was issued in.

This unlocks being able to do things like set custom reminders, open tickets from messages, and more. You can also consider use cases where the context of a specific message would be useful for things like creating a ticket in a helpdesk (like Zendesk) or bug tracking software (like JIRA).

Go to app's **Interactivity & Shortcuts** page.

In the **Shortcuts** section, click on **Create a Shortcut**, select the button for customizing **message shortcuts**, and enter the following information:

1. **Action Name**: 'Remember This!'
2. **Short Description:** 'An easy way to save interesting posts for later reference'
3. **Callback ID:** 'save4later-dgl'

Click on **Create**.

Click on **Save Changes**.

Run the script *'messageshortcuts/app.py'*. 

Post a message in any channel. Click on message shortcuts and choose the shortcut you just built. 

You should receive a DM from the app with the messaged you wanted to save. 

### Exercise 7. Interactivity

With the user token your app can impersonate another user to send a message as them on their behalf. Posting on behalf of someone else has many useful applications like, for example, the app could have a flow to work with the CEO and their executive assistant during install so the EA could actually use the app to post an announcement on behalf of the CEO.

Go to **OAuth & Permissions**.

Add the `channels.read` and `chat.write` User Token Scopes.

Add your **User OAuth Token** to your .env file.

Create a new slack channel called "Birthdays" and copy the channel ID.















