
# Telegram Message Forwarding Bot

A highly modular and customizable Telegram bot framework designed to monitor messages in specific groups, track messages from designated users, and forward them to another bot. This project allows for easy configuration and extensibility, making it a perfect starting point for your Telegram bot needs.

## Features

- **Dynamic Configuration**: Easily configure settings via the `config.json` file.
- **Message Tracking**: Monitor specific users' messages in designated groups.
- **Message Forwarding**: Automatically forward tracked messages to another bot.
- **Modular Design**: Clean and modular codebase for easy maintenance and scalability.
- **Logging**: Comprehensive logging for activity monitoring.

## Getting Started

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your machine.
- **Telegram API Credentials**: Obtain `api_id` and `api_hash` from [Telegram API](https://my.telegram.org/apps).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/telegram-bot-project.git
   cd telegram-bot-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

To configure the bot, edit the `config.json` file with your specific settings:
```json
{
    "api_id": "123456",
    "api_hash": "your_api_hash",
    "group_ids": [-100123456789, -100987654321],
    "tracked_usernames": ["username1", "username2"],
    "forward_bot_username": "your_forward_bot",
    "enable_forwarding": true
}
```

- **api_id**: Your Telegram API ID.
- **api_hash**: Your Telegram API hash.
- **group_ids**: List of group/channel IDs to monitor.
- **tracked_usernames**: List of usernames to track.
- **forward_bot_username**: The username of the bot where messages will be forwarded.
- **enable_forwarding**: Set to `true` to enable catching crypto message forwarding.

### Run the Bot

Start the bot using the following command:
```bash
python bot.py
```

## Project Structure

```plaintext
project/
├── bot.py          # Main script to start the bot
├── config.py       # Module for loading configurations
├── utils/          # Utility functions and event handlers
│   ├── logger.py   # Logging utilities
│   └── handlers.py # Event handler functions
├── config.json     # Dynamic configuration file
├── requirements.txt# Python dependencies
└── README.md       # Project documentation
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or issues, contact:

- **GitHub Issues**: Open an issue on this repository.
