# Example Configuration for Docker Notifier

This directory contains an example setup for **Docker Notifier**, including:

- `config.json`: A template configuration file for the service.
- `docker-compose.yml`: A ready-to-use Docker Compose configuration file.

## Usage

1. Edit config.json

Update the config.json file with your settings:

- `hostname`: Your host name.
- `bot_token`: Your Telegram bot token.
- `chat_ids`: Chat IDs to receive notifications.
- `exit_chat_ids`: Chat IDs to receive crash notifications.

2. Run the service

Use Docker Compose to start the service:

```bash
docker compose up -d
```

That's it! The notifier will start monitoring your Docker containers and sending notifications to Telegram.
