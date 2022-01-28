import os
import json
import discord
from dotenv import load_dotenv

from neuralintents import GenericAssistant

with open('intents.json','r',encoding='utf-8') as fp:
    data = json.loads(fp.read())

with open('intents.json','w',encoding='utf-8') as fp:
    fp.write(json.dumps(data,indent=2))

chatbot = GenericAssistant('intents.json')
# chatbot.train_model()
# chatbot.save_model()
chatbot.load_model()

class MyClient(discord.Client):
    async def on_ready(self):
        print('目前登入身份：', client.user)
        
    async def on_message(self, message:discord.Message):
        if message.author == client.user:
            return
        print (message.content, message.channel)
        response = chatbot.request(message.content)
        await message.channel.send(response)

load_dotenv()

TOKEN = os.getenv('TOKEN')

print (f"Bot running ...")

client = MyClient()

client.run(TOKEN)