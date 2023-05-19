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

Run the script *'messagemenus.py'*. 

Keep in mind that you must do this in a channel the app belongs to or in a DM with the application or this will not work.

### Exercise 5. Custom Unfurls

Go to **OAuth & Permissions** page and add `links:read` and `links:write` under **Bot Token Scopes**.

Go to **Event Subscriptions**. 

Under **Subscribe to Bot Events**, subscribe to the `link_shared` event.

In the **App Unfurl Domains** section select **Add Domain.**

Enter the example domain, 'xyz.example.com', and press **Done**.

Press **Save Changes** and then reinstall your application.

Post `https://xyz.example.com` in a DM to the App. You should see an unfurled URL returned.










