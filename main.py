import os
import discord
from dotenv import load_dotenv

from neuralintents import GenericAssistant

chatbot = GenericAssistant()

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client()

async def on_message(message:discord.Message):
    if message.author == client.user:
        return
    
    if str(message.content).startswith('$aibot'):
        pass
    

client.run(TOKEN)