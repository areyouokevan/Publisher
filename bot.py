import discord
import config
from discord.http import Route

class Publisher(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Game('https://git.io/Jfaae'))

    async def on_message(self, message):
        if message.channel.id in config.channels:
            await self.http.request(
                Route('POST', '/channels/{}/messages/{}/crosspost'.format(
                    message.channel.id,
                    message.id
                )))


bot = Publisher()
bot.run(config.token)
