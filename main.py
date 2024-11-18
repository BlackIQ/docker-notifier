import requests
import docker
import time
import os

first_time = True

amir_chat_id = 6371168857
dev_chat_id = -4040648190
noc_chat_id = -1002372829101

hostname = os.getenv("HOST_NAME", "Unknown Host")

def send_message(message, chat_id):
    bot_token = '8004860601:AAEMpaK6oT_Z27Od9fyzAJkb7RGAELgONeE'
        
    data = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage", data=data)

def main():
    client = docker.from_env()
    container_status = {}
        
    if first_time:
        messages = [
            "🐳 Docker Notifier",
            "",
            "Service is running...",
            f"Host: #{hostname}"
        ]
        
        message = "\n".join(messages)
        
        send_message(message, amir_chat_id)
    
    try:
        while True:
            running_containers = client.containers.list(all=True)
            current_status = {container.name: container.status for container in running_containers}

            for name, status in current_status.items():
                if name not in container_status or container_status[name] != status:
                    container = client.containers.get(name)
                    container_image = container.image.tags[0] if container.image.tags else "Unknown"
                    container_id = container.short_id
                    
                    exit_code = None
                    if status == "exited":
                        exit_code = container.attrs['State']['ExitCode']
                        
                        if exit_code == 0:
                            reason = "Container stopped successfully."
                        elif exit_code == 137:
                            reason = "Container killed (possibly due to resource constraints)."
                        elif exit_code == 139:
                            reason = "Container crashed (segmentation fault)."
                        else:
                            reason = f"Container exited with code {exit_code}."

                        messages = [
                            "⚠️ Problem ⚠️",
                            "🐳 Container Down",
                            f"Problem started at {time.strftime('%H:%M:%S on %Y.%m.%d')}❗️",
                            f"📦 Container name: #{name}",
                            f"Container id: {container_id}",
                            f"Container image: {container_image}",
                            f"Host: #{hostname}",
                            f"Exit code: {exit_code}",
                            f"Reason: {reason}"
                        ]
                        
                        message = "\n".join(messages)

                        if not first_time:
                            send_message(message, amir_chat_id)
                            # send_message(message, noc_chat_id)
                        
                            # if exit_code != 0:
                                # send_message(message, dev_chat_id)
                        
                        container_status[name] = status
                    elif status == "running":
                        messages = [
                            "✅ Resolved ✅",
                            "🐳 Container Running",
                            f"Problem resolved at {time.strftime('%H:%M:%S on %Y.%m.%d')}❗️",
                            f"📦 Container name: #{name}",
                            f"Host: #{hostname}",
                            f"Container id: {container_id}",
                            f"Container image: {container_image}"
                        ]
                        
                        message = "\n".join(messages)
                        
                        if not first_time:
                            send_message(message, amir_chat_id)
                            # send_message(message, noc_chat_id)
                        
                            # if exit_code != 0:
                                # send_message(message, dev_chat_id)
                                
                        container_status[name] = status

            for name in list(container_status.keys()):
                if name not in current_status:
                    messages = [
                        "⚠️ Problem ⚠️",
                        "🐳 Container Removed",
                        f"Problem started at {time.strftime('%H:%M:%S on %Y.%m.%d')}❗️",
                        f"📦 Container name: #{name}",
                        f"Host: #{hostname}",
                        f"Container id: Unknown (removed)",
                        "Container image: Unknown (removed)"
                    ]
                    
                    message = "\n".join(messages)
                    
                    send_message(message, amir_chat_id)
                    # send_message(message, noc_chat_id)
                    
                    del container_status[name]

            time.sleep(5)
    except KeyboardInterrupt:
        messages = [
            "🐳 Docker Notifier",
            "",
            "Service is stopped...",
            f"Host: #{hostname}"
        ]
        
        message = "\n".join(messages)
        
        send_message(message, amir_chat_id)
        # send_message(message, noc_chat_id)
    except Exception as e:
        messages = [
            "🐳 Docker Notifier",
            "",
            "Service has error...",
            f"Host: #{hostname}",
        ]
        
        message = "\n".join(messages)
        
        send_message(message, amir_chat_id)
        # send_message(message, noc_chat_id)
        
if __name__ == "__main__":
    main()
