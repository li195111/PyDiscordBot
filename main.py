# encoding: utf-8

import os
import discord
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('目前登入身份：', self.user)
        
    async def on_message(self, message:discord.Message):
        if message.author == self.user:
            return
        await message.channel.send(f'你在 {message.channel} 說： {message.content}')
        
if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    client = MyClient()
    client.run(TOKEN)