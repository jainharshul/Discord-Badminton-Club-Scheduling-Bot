import discord
import os
from discord import embeds
from discord.ext import commands
import copy
from webserver import keep_alive

my_secret = os.environ['DISCORD_BOT_SECRET']
bot = commands.Bot(command_prefix='#')

timeswithnames = ["6am: ", "7am: ", "8am: ", "9am: ", "10am: ", "11am: ", "12pm: ", "1pm: ", "2pm: ", "3pm: ", "4pm: ", "5pm: ", "6pm: "]

bot.remove_command('help')


@bot.command()
async def help(ctx):
    side = discord.Embed(title='Help',
                         description='Here here are all the commands aviailable to use!',
                         colour=discord.Colour.blue())
    side.add_field(name='#join', value="followed with time including am/pm adds you to the schedule", inline=False)
    side.add_field(name='#canceljoin', value="removes you from the schedule", inline=False)
    side.add_field(name='#schedule', value="shows the times with everyone signed up", inline=False)
    side.add_field(name='#clearschedule', value="reformats the whole schedule for a new day", inline=False)
    await ctx.send(embed=side)


@bot.command()
async def clearschedule(ctx):
    timeswithnames[0] = "6am: "
    timeswithnames[1] = "7am: "
    timeswithnames[2] = "8am: "
    timeswithnames[3] = "9am: "
    timeswithnames[4] = "10am: "
    timeswithnames[5] = "11am: "
    timeswithnames[6] = "12pm: "
    timeswithnames[7] = "1pm: "
    timeswithnames[8] = "2pm: "
    timeswithnames[9] = "3pm: "
    timeswithnames[10] = "4pm: "
    timeswithnames[11] = "5pm: "
    timeswithnames[12] = "6pm: "
    await ctx.channel.send("The schedule has been reset!")


@bot.command()
async def join(ctx, message=None):
    user = ctx.author.name
    if message == "6am":
        timeswithnames[0] = timeswithnames[0] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 6am!")
    elif message == "7am":
        timeswithnames[1] = timeswithnames[1] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 7am!")
    elif message == "8am":
        timeswithnames[2] = timeswithnames[2] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 8am!")
    elif message == "9am":
        timeswithnames[3] = timeswithnames[3] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 9am!")
    elif message == "10am":
        timeswithnames[4] = timeswithnames[4] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 10am!")
    elif message == "11am":
        timeswithnames[5] = timeswithnames[5] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 11am!")
    elif message == "12pm":
        timeswithnames[6] = timeswithnames[6] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 12pm!")
    elif message == "1pm":
        timeswithnames[7] = timeswithnames[7] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 1pm!")
    elif message == "2pm":
        timeswithnames[8] = timeswithnames[8] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 2pm!")
    elif message == "3pm":
        timeswithnames[9] = timeswithnames[9] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 3pm!")
    elif message == "4pm":
        timeswithnames[10] = timeswithnames[10] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 4pm!")
    elif message == "5pm":
        timeswithnames[11] = timeswithnames[11] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 5pm!")
    elif message == "6pm":
        timeswithnames[12] = timeswithnames[12] + ", " + user
        await ctx.channel.send("Congrats " + user + " you are signed up for 6pm!")


@bot.command()
async def canceljoin(ctx):
    user = ctx.author.name
    for x in range (13):
        if user in timeswithnames[x]:
            teststring = timeswithnames[x].replace(", " + user, "")
            timeswithnames[x] = teststring
    await ctx.channel.send("You have been removed from the schedule!")


@bot.command()
async def schedule(ctx):
    side = discord.Embed(title = 'Schedule',
                          description= 'Here is the current schedule with all players',
                          colour= discord.Colour.blue())
    one = timeswithnames[0]
    two = timeswithnames[1]
    three = timeswithnames[2]
    four = timeswithnames[3]
    five = timeswithnames[4]
    six = timeswithnames[5]
    seven = timeswithnames[6]
    eight = timeswithnames[7]
    nine = timeswithnames[8]
    ten = timeswithnames[9]
    eleven = timeswithnames[10]
    twelve = timeswithnames[11]
    thirteen = timeswithnames[12]



    side.add_field(name = '.', value = one, inline = False)
    side.add_field(name = '.', value = two, inline = False)
    side.add_field(name = '.', value = three, inline = False)
    side.add_field(name = '.', value = four, inline = False)
    side.add_field(name = '.', value = five, inline = False)
    side.add_field(name = '.', value = six, inline = False)
    side.add_field(name = '.', value = seven, inline = False)
    side.add_field(name = '.', value = eight, inline = False)
    side.add_field(name = '.', value = nine, inline = False)
    side.add_field(name = '.', value = ten, inline = False)
    side.add_field(name = '.', value = eleven, inline = False)
    side.add_field(name = '.', value= twelve, inline=False)
    side.add_field(name ='.', value= thirteen, inline=False)


    await ctx.send(embed=side)

keep_alive()
bot.run(my_secret)