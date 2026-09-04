# Telegram Channel Invite Bot

A simple Telegram bot that welcomes users and provides a button to join a Telegram channel.

## Features

- Welcomes users with a friendly message when they start the bot
- Provides a single inline button to join a specific Telegram channel
- Simple, focused functionality
- No database required
- No user data collection

## Prerequisites

- Python 3.12+
- A Telegram Bot Token from BotFather
- A Telegram channel (or group) invite link

## Setup

### 1. Create the Bot with BotFather

1. Open Telegram and search for `@BotFather`
2. Start a chat with BotFather
3. Send `/newbot` command
4. Choose a name for your bot (e.g., "My Channel Bot")
5. Choose a username for your bot (must end with `bot`, e.g., `my_channel_bot`)
6. BotFather will provide you with a token - **save this token securely**

### 2. Create a GitHub Repository

1. Go to GitHub.com and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., "telegram-channel-bot")
4. Choose "Public" or "Private" (Public is free, Private requires payment)
5. Click "Create repository"

### 3. Upload Files to GitHub

1. Clone your repository locally or use GitHub's web interface
2. Upload all the files from this project:
   - `bot.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `.gitignore`
   - `README.md`
3. Commit and push the changes

### 4. Deploy to Railway

1. Go to Railway.app and sign up/sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account if not already connected
5. Select the repository you created
6. Railway will automatically detect your project

### 5. Add Environment Variables

1. In your Railway project dashboard, click on your deployed service
2. Go to the "Variables" tab
3. Click "Add Variable"
4. Enter `BOT_TOKEN` as the variable name
5. Paste your bot token from BotFather as the value
6. Click "Save"

### 6. Deploy

1. Railway will automatically deploy your project
2. Watch the logs to ensure everything starts successfully
3. Once deployed, Railway will provide a URL (though not needed for Telegram bots)

### 7. Test Your Bot

1. Open Telegram and search for your bot's username
2. Send `/start` to your bot
3. You should see the welcome message and the "Join Our Channel" button
4. Click the button to verify it opens your channel invite link

## How It Works

When a user sends `/start` to the bot:

1. The bot responds with a welcome message
2. A button labeled "🚀 Join Our Channel" appears below the message
3. Clicking the button opens the Telegram channel invite link

## Important Notes

- The bot only responds to `/start` commands
- No user data is collected or stored
- No database is required
- The bot does not have any hidden or extra features

## File Structure
