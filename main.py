import asyncio
import discord
import os
import sys
import traceback
import subprocess
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# For invite
perm_int = '116800'

# Environment variables
app_id = str(os.getenv('APP_ID'))
bot_token = str(os.getenv('BOT_TOKEN'))

# Get owners
owners: list[int] = []
owners_env = str(os.getenv('OWNER_IDS'))
if owners_env:
    for entry in owners_env.replace(' ', '').split(','):
        maybe_entry = int(entry)
        if maybe_entry:
            owners.append(maybe_entry)

def is_owner(owner_id: int):
    for owner in owners:
        if owner_id == owner:
            return True
    return False


class SimpleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        if is_owner(ctx.author.id):
            await ctx.send('https://discord.com/oauth2/authorize/?permissions='+ perm_int +'&scope=bot&client_id=' + app_id)

    @commands.command()
    async def do(self, ctx, shortcut):
        if is_owner(ctx.author.id):
            # Send status
            await ctx.send(f'Running shortcut {shortcut}')
            cmd = [os.getcwd() + '/do.sh', shortcut]
            p = subprocess.run(cmd, capture_output=True, text=True)
            output = p.stdout + p.stderr
            await ctx.send(f'Processed shortcut! Return code `{p.returncode}`, output: ```{output}```')

    @commands.command()
    async def stopserver(self, ctx):
        if is_owner(ctx.author.id):
            res = os.spawnlp(os.P_WAIT, '/bin/date' , 'stop dougcraft')
            await ctx.send(f'Stopping server! Return code `{res}`')


# Create bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("m!"),
    intents=intents,
)


# Log bot login
@bot.event
async def on_ready():
    if bot.user:
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    else:
        print('Logged in')


# Log command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("I could not find member '{error.argument}'. Please try again")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"'{error.param.name}' is a required argument.")
    else:
        print(f'*** Exception in command "{ctx.command}" ***', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


# Start bot
async def main():
    async with bot:
        await bot.add_cog(SimpleCommands(bot))
        await bot.start(bot_token)

asyncio.run(main())
