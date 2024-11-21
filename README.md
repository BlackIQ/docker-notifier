# Docker Containers Notifier

**Docker Notifier** is a service that listens to container status events and sends notifications to Telegram.

## Pull the Image

To pull the latest Docker image, use the following command:

```bash
docker pull blackiq/docker-notifier:latest
```

## Configuration

You need to provide some essential configuration values such as **Bot Token**, **Chat IDs**, and a **Hostname**.
Create a config.json file with the following structure:

```json
{
  "hostname": "your_host_name",
  "bot_token": "bot_token",
  "chat_ids": [1234, -9876],
  "exit_chat_ids": [4321, -6789]
}
```

- `hostname`: Identifies the host in notifications.
- `bot_token`: Token for your Telegram bot. Create a bot via @BotFather on Telegram.
- `chat_ids`: IDs of Telegram chats to receive all status notifications.
- `exit_chat_ids`: IDs of Telegram chats to receive crash notifications only.

Ensure the config.json file is mounted to /etc/docker-notifier/config.json when running the container.

## Running the Service

You can run the service using either the command line or Docker Compose.

### Using Command Line

Ensure the `config.json` file is ready, then run the container with the following command:

```bash
docker run -d \
  --name docker-notifier \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/config.json:/etc/docker-notifier/config.json \
  blackiq/docker-notifier:latest
```

### Using Docker Compose

Here’s an example `docker-compose.yml` configuration:

```yaml
version: "3"

services:
  docker-notifier:
    image: blackiq/docker-notifier:latest
    container_name: docker-notifier
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /path/to/config.json:/etc/docker-notifier/config.json
    restart: always
```

Run the service with:

```bash
docker compose up -d
```

## Example Setup

For a quicker setup, clone the repository and use the provided example directory:

```bash
git clone https://github.com/BlackIQ/docker-notifier.git
cd docker-notifier/example
```

Edit the `config.json` file in the example directory to match your configuration, then start the service:

```bash
docker compose up -d
```

## Contributing

We’re always looking to improve **Docker Notifier** and would love your help! If you have ideas for features, bug fixes, or enhancements, feel free to contribute.

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed explanation.

Your feedback and contributions are greatly appreciated!
