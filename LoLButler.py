import discord

TOKEN = 'NDMxODk5ODYxMDAxMTc1MDQy.Daldmw.4WSYLBsRFap20xXtrjnIM2Wd2yE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #this will list all the commands the bot can execute
    if message.content.upper().startswith('!HELP'):
        await client.send_message(message.channel, 'Thank you for using LoL Butler! Please see the list of commands below.\n\n!help: this will list all the commands the bot can execute\n!look up [region code] [summoner name]: this will look up a player on op.gg database\n\t\tFor example: !look up euw xlarb\n!info [champion name]: this will return a link containing info about a specific champion\n\t\tFor example: !info vayne\n!build [champion name]: this will return a link containing info about the best builds for a specific champion\n\t\tFor example: !build alistar\n!counter [champion name]: this will return a link containing info about the best counter for a specific champion\n\t\tFor example: !counter darius\n\n' + ' {0.author.mention}'.format(message))
    #this will look up a player on the eune server
    elif message.content.upper().startswith('!LOOK UP EUNE'):
        temp = message.content[13:].replace(' ', '');
        msg = 'http://eune.op.gg/summoner/userName=' + temp + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #this will look up a player on op.gg database
    elif message.content.upper().startswith('!LOOK UP'):
        temp1 = message.content[9:12].replace(' ', '');
        temp2 = message.content[12:].replace(' ', '');
        msg = 'http://' + temp1 + '.op.gg/summoner/userName=' + temp2 + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #this will return a link containing info about a specific champion
    elif message.content.upper().startswith('!INFO'):
        temp = message.content[5:].replace(' ', '');
        msg = 'http://champion.gg/champion/' + temp + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #this will return a link containing info about the best builds for a specific champion
    elif message.content.upper().startswith('!BUILD'):
        temp = message.content[6:].replace(' ', '');
        msg = 'http://www.probuilds.net/champions/details/' + temp + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #this will return a link containing info about the best counter for a specific champion
    elif message.content.upper().startswith('!COUNTER'):
        temp = message.content[8:].replace(' ', '');
        msg = 'http://www.championcounter.com/' + temp + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
client.run(TOKEN)
