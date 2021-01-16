import os
import discord
import command_manager
from dotenv import load_dotenv


load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message (message):
    if message.author == client.user:
        pass
    else:
        channel = message.channel
        # print message content
        message_content = message.content
        tokens = message_content.split(" ")
        if tokens==[]:
            return
        if tokens[0].lower()=="?doc":
            print("here")
            reply = command_manager.run_request(tokens)
            await channel.send(reply)
        return True
        

client.run("Nzk5NzczMjYwNjk3OTYwNDky.YAIc5A._KhttkNRR0ItvmM1wOPL2ew7FgE")
client = discord.Client()