# encoding: utf-8

import json
import os

import discord
from dotenv import load_dotenv
from neuralintents import GenericAssistant

class MyClient(discord.Client):
    async def on_ready(self):
        print('目前登入身份：', self.user)
        
    async def on_message(self, message:discord.Message):
        if message.author == self.user:
            return
        response = chatbot.request(message.content)
        await message.channel.send(response)

class GenericAssistantProxy(GenericAssistant):
    def __init__(self, intents, intent_methods=..., model_name="assistant_model"):
        self.rewrite_intents_file(intents)
        super().__init__(intents, intent_methods, model_name)

    def rewrite_intents_file(self, file_path):
        '''To avoid encoding error'''
        with open(file_path,'r',encoding='utf-8') as fp:
            data = json.loads(fp.read())
        with open(file_path,'w',encoding='utf-8') as fp:
            fp.write(json.dumps(data,indent=1))

if __name__ == "__main__":
    chatbot = GenericAssistantProxy('intents.json')
    model_path = f'{chatbot.model_name}.h5'
    if not os.path.exists(model_path):
        chatbot.train_model()
        chatbot.save_model()
    else:
        chatbot.load_model()
    
    print (f"Bot running ...")
    
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    
    client = MyClient()
    client.run(TOKEN)
