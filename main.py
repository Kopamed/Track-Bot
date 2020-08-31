import os
import random
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='k')




def load_json(file_name):
    with open(file_name, "r") as write_file:
        data = write_file.read()
        data = json.loads(data)
    return data



def dump_json(file_name, data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file)



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    
    
@bot.event
async def on_member_update(before, after):
    
    data = load_json("data.json")
    
    if str(after.id) in data and data[str(after.id)]["notify"] == "True":
        
        print("In data")
        print(int(data[str(after.id)]["trackedByID"]))

        member = await bot.fetch_user(int(data[str(after.id)]["trackedByID"]))
        await member.create_dm()
        await member.dm_channel.send("{} has gone {}.".format(after,after.status))
        
        print("sent message to {}".format(data[str(after.id)]["trackedByUser"]))
        




@bot.command(name='track', help='Starts tracking a person of your choice')
async def track(ctx):
    
    print(ctx.author.avatar_url)
    response = ctx.guild.members
    await ctx.send(response)
    await ctx.send(ctx.author.avatar_url)
    
    

bot.run(TOKEN)