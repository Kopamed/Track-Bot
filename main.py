import os
import random
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='k')

"""
def create_track(trackerID, trackerU, trackedID, trackedU):
    data = load_json("data.json")
    dat
"""



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
        print(data[str(after.id)]["trackedByID"])
        
        for i in range(len(data[str(after.id)]["trackedByID"])):
            
            member = await bot.fetch_user(int(data[str(after.id)]["trackedByID"][i]))
            await member.create_dm()
            await member.dm_channel.send("{} has gone {}.".format(after,after.status))
            
            print("sent message to {} about {}".format(data[str(after.id)]["trackedByUser"], data[str(after.id)]["trackedByUser"][i]))
        




@bot.command(name='track', help='Starts tracking a person of your choice. e.g. ktrack @Kopamed')
async def track(ctx, tag):
    
    print(tag[3:-1])
    
    

bot.run(TOKEN)