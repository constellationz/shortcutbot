# Bash shortcut bot

A Discord bot that lets you set up simple bash shortcuts

## Install

1. Clone this repository to a user with the correct permissions

```bash
apt-get install git python3 python3-pip python3-venv -y
adduser shortcutbot
login shortcutbot
git clone https://git.tylerlab.org/tyler/shortcutbot.git
cd shortcutbut
./setup.sh
```

2. Set up the `.env` file and `do.sh` file.

```
# env
APP_ID="<your app id>"
BOT_TOKEN="<your bot token>"
```

```bash
# do.sh
start)
    systemctl start minecraft.service
    ;;
```

3. Install the systemd service with this command:

```bash
sudo install /etc/systemd/system/ shortcutbot.service
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
