import os
import random
import asyncio
import json
import discord
from discord.ext import commands
import datetime

with open(".gitignore/token", "r") as f:
    TOKEN = f.read()


bot = commands.Bot(command_prefix='t.', case_insensitive=False)

"""
def create_track(trackerID, trackerU, trackedID, trackedU):
    data = load_json("data.json")
    data
"""



def load_json(file_name):
    with open(file_name, "r") as write_file:
        data = write_file.read()
        data = json.loads(data)
    return data



def dump_json(file_name, data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file, indent = 4)



@bot.event
async def on_ready():
    await bot.loop.create_task(servercount())

async def servercount():
    await bot.wait_until_ready()
    while not bot.is_closed():
        count = 0
        for i in bot.guilds:
            count+= len(i.members)
        
        await bot.change_presence(
            activity=discord.Game(
                name=f"t.help for {count} users", type=1))

        await asyncio.sleep(60)

    
@bot.event
async def on_member_update(before, after):
    
    
    
    data = load_json("data.json")
    
    
    
    if str(after.id) in data and data[str(after.id)]["previous"] != str(after.status[0]):
        
        
        
        
        
        data[str(after.id)]["previous"] = str(after.status[0])
        dump_json("data.json", data)
        
        
        for i in range(len(data[str(after.id)]["trackedByID"])):
            
            member = await bot.fetch_user(int(data[str(after.id)]["trackedByID"][i]))
            await member.create_dm()
            
            embed= discord.Embed(
                title="{} is now".format(after),
                description="`{}`".format(str(after.status[0]).upper()),
                colour=discord.Colour(0x187bcd))
                
            embed.set_footer(
                text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
                
            embed.set_author(
                name="Track Bot - {}".format(datetime.datetime.now()), url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
                
            embed.set_thumbnail(
                url = str(after.avatar_url))
            
            
            
            
            #embed = discord.Embed(title=f"{member} just joined the server!", colour = 0xffa500)
                
            #embed.set_image(url=f"attachment://{filename}")
                
            #file=(file, embed=embed)
            await member.dm_channel.send(content=None, embed=embed)
            
            print("sent message to {} about {}".format(data[str(after.id)]["trackedByUser"][i], data[str(after.id)]["username"]))
            




@bot.command(name='track', help='Starts tracking a person of your choice. e.g. t.track @Kopamed')
async def track(ctx, tag):
    
    data = load_json("data.json")
   
    print(tag)
    print(tag[3:-1])
    target_id = str(tag[3:-1])
    
    
    try:
        target = await bot.fetch_user(int(target_id))
    except:
        target_id = str(tag[2:-1])
        target = await bot.fetch_user(int(target_id))
    
    if target_id in data:
        if str(ctx.author.id) in data[target_id]["trackedByID"]:
            
            
            
            embed= discord.Embed(
            title="You are already tracking that user",
            description="You are already tracking {}!". format(target),
            colour=discord.Colour(0x187bcd))
            embed.set_footer(
            text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
            embed.set_author(
            name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
            embed.set_thumbnail(
            url = str(target.avatar_url))
            
            await ctx.send(content = None, embed=embed)
            
            return
            
            
        else:
            
            data[target_id]["trackedByID"].append(str(ctx.author.id))
            data[target_id]["trackedByUser"].append(str(ctx.author))
    
    else:
        data[target_id] = {"trackedByID": [str(ctx.author.id)], "trackedByUser": [str(ctx.author)], "username": str(target), "premium": "False", "notifySelf": "True", "previous": "unknown"}
        
    dump_json("data.json", data)
    
    embed= discord.Embed(
        title="Tracking Successfully",
        description="You are now tracking {}". format(target),
        colour=discord.Colour(0x187bcd))
    embed.set_footer(
        text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
    embed.set_author(
        name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
    embed.set_thumbnail(
        url = str(target.avatar_url))
  
    await ctx.send(content = None, embed=embed)
    
    
    
    
    
    
    
@bot.command(name='wait', help='1 time notification of when a user goes ____. e.g. t.wait @Kopamed online | available options: offline, online, dnd, idle')
async def track(ctx, tag, state):
    
  
    await ctx.send("Feature coming soon!")
    
    
    
    
    
@bot.command(name='notify', help='You can choose what status notifies you. FOr example you only want to get notified when your friend goes offline and not online. e.g. t.notify online true | available options: offline, online, dnd, idle, settings | available states: off, on')
async def track(ctx, status, option):
    
    statuses = ["online", "offline", "dnd", "idle", "settings"]
    states = ["off", "on"]
    
    if status not in statuses:
        await ctx.send("Feature coming soon!")
        
    await ctx.send("Feature coming soon!")
    
    
    
    
    
    
    




@bot.command(name='traceback', help='Shows you who is tracking you. e.g. t.traceback')
async def traceback(ctx):
    
    data = load_json("data.json")
    
    if str(ctx.author.id) in data and data[str(ctx.author.id)]["premium"] == "True":
        
        
        if len(data[str(ctx.author.id)]["trackedByID"]) == 0:
            embed= discord.Embed(
            title="You are being tracked by",
            description="No one. Yes, no one cares about you.",
            colour=discord.Colour(0x187bcd))
            embed.set_footer(
            text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
            embed.set_author(
            name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
            embed.set_thumbnail(
            url = str(ctx.author.avatar_url))
            
            
        else:
            
    
            embed= discord.Embed(
            title="You are being tracked by",
            description=", ".join(i for i in data[str(ctx.author.id)]["trackedByUser"]),
            colour=discord.Colour(0x187bcd))
            embed.set_footer(
            text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
            embed.set_author(
            name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
            embed.set_thumbnail(
            url = str(ctx.author.avatar_url))
        
    
    else:
        
        embed= discord.Embed(
        title="You need to have premium to be able to perform this command!",
        description="You can not currently buy premium, but we are working on getting it to you!",
        colour=discord.Colour(0x187bcd))
        embed.set_footer(
        text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
        embed.set_author(
        name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
        embed.set_thumbnail(
        url = str(ctx.author.avatar_url))
        
    
  
    await ctx.send(content = None, embed=embed)
    







    



@bot.command(name='lose', help='Stops tracking a person of your choice. e.g. t.lose @Kopamed')
async def lose(ctx, tag):
    
    data = load_json("data.json")
    
    print(tag)
    print(tag[3:-1])
    target_id = str(tag[3:-1])
    
    
    try:
        target = await bot.fetch_user(int(target_id))
    except:
        target_id = str(tag[2:-1])
        target = await bot.fetch_user(int(target_id))
    
    if target_id in data:
        data[target_id]["trackedByID"].remove(str(ctx.author.id))
        data[target_id]["trackedByUser"].remove(str(ctx.author))
    
    else:
        
        embed= discord.Embed(
        title="You are not tracking that user",
        description="You were not tracking {} in the first place". format(target),
        colour=discord.Colour(0x187bcd))
        embed.set_footer(
        text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
        embed.set_author(
        name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
        embed.set_thumbnail(
        url = str(target.avatar_url))
        
        await ctx.send(content = None, embed=embed)
        
        return
        
        
        
        
        
    dump_json("data.json", data)
    
    embed= discord.Embed(
        title="Lost Successfully",
        description="You are now not tracking {}". format(target),
        colour=discord.Colour(0x187bcd))
    embed.set_footer(
        text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
    embed.set_author(
        name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
    embed.set_thumbnail(
        url = str(target.avatar_url))
  
    await ctx.send(content = None, embed=embed)
    

    

    
    
    
@bot.command(name='ping', help='Returns your ping')
async def ping(ctx):
    embed= discord.Embed(
    title="Pong",
    description="`{0}ms`". format(round(bot.latency * 100, 0)),
    colour=discord.Colour(0x187bcd))
    embed.set_footer(
    text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
    embed.set_author(
    name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
    embed.set_thumbnail(
    url = str(ctx.author.avatar_url))
  
    await ctx.send(content=None,embed=embed)
  
  
 
@bot.command(name='inv', help='Lets you invite the bot to your server')
async def inv(ctx):
    embed= discord.Embed(
    title="Invite Link",
    colour=discord.Colour(0x187bcd))
    embed.add_field(name="URL", value="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
    embed.set_footer(
    text="https://discord.com/oauth2/authorize?client_id=749989132763136021&permissions=8&scope=bot")
    embed.set_author(
    name="Track Bot", url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg", icon_url= "https://media.wired.com/photos/5b6df22751297c21002b4536/2:1/w_2400,h_1200,c_limit/HackerBot.jpg")
    embed.set_thumbnail(
    url = str(ctx.author.avatar_url))
  
    await ctx.send(content=None,embed=embed)
  
  
bot.run(TOKEN)