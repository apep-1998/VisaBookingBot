# Appointment Booking Bot for otv.verwalt-berlin.de

This repository contains a Python bot that uses the Selenium library and the Chrome browser to book appointments from the otv.verwalt-berlin.de website. The bot continuously checks for available time slots and, if found, proceeds to make a reservation and sends a message on Telegram.

## How to Run

To run the bot, follow the steps below:

1. Install Python: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. Install Chrome Browser: If you don't have the Chrome browser installed, download and install it from the [official Chrome website](https://www.google.com/chrome/).

3. Get the Code: Clone the repository or download the code.

```bash
git clone https://github.com/apep-1998/VisaBookingBot.git
cd VisaBookingBot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Configuration: Open the `config.py` file and configure the required values based on your information. Some of the settings you need to specify include:

- `TELEGRAM_API_TOKEN`: Your Telegram API token.
- `TELEGRAM_CHAT_ID`: The chat ID where the bot will send messages.
- Other relevant settings such as website URLs, credentials, etc.

5. Run the Bot: Execute the following command to run the bot:

```
source venv/bin/activate
python main.py
```

Please note that the bot is designed to work specifically with the otv.verwalt-berlin.de website. Make sure to provide the correct configurations and adapt the code accordingly if you intend to use it with a different website.

**Disclaimer:** Use this bot responsibly and in compliance with the terms of use of the website you are automating.
