#!/usr/bin/env bash
# Sets up environment
python3 -m venv .venv
.venv/bin/pip3 install -r requirements.txt
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Edit .env to configure the bot"
fi
if [ ! -f do.sh ]; then
    cp example_do.sh do.sh
    echo "Edit do.sh to configure shortcuts"
fi
