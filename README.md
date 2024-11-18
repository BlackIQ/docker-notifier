# Docker Containers Notifier

## Build

```bash
docker build -t docker-notifier .
```

## Run

```bash
docker run -d \
  --name docker-notifier \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker-notifier
```