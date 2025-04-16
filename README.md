# Bash shortcut bot

A Discord bot that lets you run simple bash shortcuts on your server.

## Install

1. Clone this repository to a user with the correct permissions

```bash
apt-get install git python3 python3-pip python3-venv -y
adduser shortcutbot
login shortcutbot
git clone https://git.tylerlab.org/tyler/shortcutbot.git
cd shortcutbot
./setup.sh
```

2. Set up the `.env` file and `do.sh` file.

You will need to add your bot's app id, your bot's token, and the IDs of the users who should be able to run commands.

```
# env
APP_ID="<your app id>"
BOT_TOKEN="<your bot token>"
OWNER_IDS="1234567890,1234567890,1234567890"
```

Making a shortcut is as simple as writing some Bash:

```bash
# do.sh
start)
    systemctl start minecraft.service
    ;;
```

3. Install the systemd service with this command:

```bash
su # Log in as root
install shortcutbot.service /etc/systemd/system/
```

4. Start the bot and view the logs like so:

```bash
systemctl enable shortcutbot.service --now
journalctl -xeu shortcutbot.service
```

## Root User Shortcuts

To add a shortcut that can run as the root user, you will have to edit `do.sh` and the sudoers file.

First, create a user group for the `shortcutbot` user:

```bash
sudo groupadd shortcutbot
```

Add the user to this group:

```bash
sudo usermod -aG shortcutbot shortcutbot
```

Now you can add your `sudo` shortcuts to the `do.sh` file.

```bash
# do.sh
start)
    sudo systemctl start minecraft.service
    ;;
stop)
    sudo systemctl stop minecraft.service
    ;;
restart)
    sudo systemctl restart minecraft.service
    ;;
```

For these to work, you will have to place the equivalent sudo commands in the sudoers file.

```bash
visudo
```

```
shortcutbot ALL=(ALL) NOPASSWD: /usr/bin/systemctl start minecraft.service
shortcutbot ALL=(ALL) NOPASSWD: /usr/bin/systemctl stop minecraft.service
shortcutbot ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart minecraft.service
```

## License

`shortcutbot` is licensed under the MIT license
