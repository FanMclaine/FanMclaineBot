#This Code sucks
#People Suck

#Bot token: Bot-Token
#never gonna give you up


# bot.py
import discord
import time

client = discord.Client()

#Login bot
@client.event
async def on_ready():
    game = discord.Game("Mcbot pls commands | V 1.14")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(f"Logged in as {client.user} Ready!")

#Maybe not an Amauteur btw here's fanmclaine bot's info
#Name: FanMclaineBot; Nickname: Mcbot; Scripting Language: Python;


#bot perspective
@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

#Commands
    if "mcbot pls question" in message.content.lower():
        await message.channel.send("Question: Do you know what **Sawcon** is?")

        if "yes" in message.content.lower():
            await message.channel.send("Now you ruined the joke!")

        else:
            await message.channel.send("SAWCON DEEZ NUTS!!!BOI!!")

    elif "mcbot?" in message.content.lower():
        await message.channel.send("Ye?")

    elif "mcbot >>>source code server id" in message.content.lower():
        await message.channel.send("Source Code Server ID:709477782828220446")

    elif "mcbot >>>fanmclainebot unofficial server id" in message.content.lower():
        await message.channel.send("FanMclaineBot Unofficial Server ID:718492380051013663") 

    elif "mcbot say a joke" in message.content.lower():
        bruhb = discord.Embed(
            title = 'Non randomized Joke',
            description = 'Microsoft Edge is so slow that it is no longer faster than my crush replies!'
        )

        bruhb.set_footer(text='Powered by some shitty code')
        bruhb.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        bruhb.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        bruhb.set_image(url='https://www.pngmart.com/files/11/LMAO-Emoji-PNG-File.png')
        
        await message.channel.send(embed=bruhb)


    elif "mcbot pls wholesome commands" in message.content.lower():
        sweet = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.red()
        )

        sweet.set_footer(text='Powered by some shitty code')
        sweet.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        sweet.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        sweet.add_field(value='Codes a motivational code using js', name='Mcbot code a motivational code')
        sweet.add_field(value='I have no idea', name='Mcbot do you love me?', inline=False)
        sweet.add_field(value='Be spitting straight fact', name='Say something about friens Mcbot', inline=False)

        await message.channel.send(embed=sweet)


    elif "mcbot code a motivational code" in message.content.lower():
        await message.channel.send("```if (give_up) { pls = 'dont'; }```")

    elif "mcbot say something about life" in message.content.lower():
        await message.channel.send("When life gives you melons, You are dyslexic")

    elif "mcbot pls commands" in message.content.lower():
        embed = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.orange()
        )

        embed.set_footer(text='Powered by some shitty code')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        embed.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        embed.add_field(value='Seems like you already knew it!', name='Mcbot pls commands')
        embed.add_field(value='Funny jokes that make me wanna commit suicide', name='Mcbot pls Funny commands', inline=False)
        embed.add_field(value='Awww, Sweet!', name='Mcbot pls Wholesome commands', inline=False)
        embed.add_field(value='Haker', name='Mcbot pls Prompt commands', inline=False)
        embed.add_field(value='Lenny face', name='Mcbot pls NSFW commands', inline=False)
        embed.add_field(value='This dscription would be long', name='Mcbot pls Social Media commands', inline=False)

        await message.channel.send(embed=embed)


    elif "mcbot >>>ping latency test" in message.content.lower():
        await message.channel.send("Checking ping...")
        await message.channel.send(f'Ping: {client.latency}ms')

    elif "hello mcbot!" in message.content.lower():
        await message.channel.send("Hi i am FanMclaineBot! call me Mcbot for short!")

    elif "mcbot do you love me?" in message.content.lower():
        await message.channel.send("Yes, of course! im always here supporting you! :heart:")

    elif "mcbot say a motivational quote" in message.content.lower():
        await message.channel.send("“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney.")

    elif "mcbot spit straight facts" in message.content.lower():
        bruhc = discord.Embed(
            title = 'Facts',
            description = 'Essential oils are only for relaxing so vaccinate your kids karen!'
        )

        bruhc.set_footer(text='Powered by some shitty code')
        bruhc.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        bruhc.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        bruhc.set_image(url='https://cdn.discordapp.com/emojis/715481003921113138.png?v=1')
        
        await message.channel.send(embed=bruhc)

    elif "mcbot say a coding pun" in message.content.lower():
        bruhb = discord.Embed(
            title = 'Coding pun',
            description = 'Why do Java programmer wear glasses? Because they cant C#!'
        )

        bruhb.set_footer(text='Powered by some shitty code')
        bruhb.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        bruhb.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        bruhb.set_image(url='https://www.pngmart.com/files/11/LMAO-Emoji-PNG-File.png')
        
        await message.channel.send(embed=bruhb)

    elif "<@!697771701127217173>" in message.content.lower():
        await message.channel.send("Hey!, How dare you ping my creator again!!")

    elif "mcbot pls help" in message.content.lower():
        await message.channel.send("`For more information about mcbot, visit: https://www.youtube.com/watch?v=dQw4w9WgXc`")

    elif "mcbot noot" in message.content.lower():
        await message.channel.send("NOOT!! NOOT!!")

    elif "mcbot are u gay?" in message.content.lower():
        await message.channel.send("No, i am Bisexual")

    elif "mcbot pls funny commands" in message.content.lower():
        embedo = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.orange()
        )

        embedo.set_footer(text='Powered by some shitty code')
        embedo.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        embedo.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        embedo.add_field(value='Funny discord screenshot', name='Mcbot send something funny')
        embedo.add_field(value='Non randomized joke', name='Mcbot say a joke', inline=False)
        embedo.add_field(value='This is not funny', name='Mcbot pls Question', inline=False)
        embedo.add_field(value='Haha htm go <br><br><br>', name='Mcbot pls say a Coding Pun', inline=False)
        embedo.add_field(value='Gungigngaggugagaga', name='Mcbot spit straight facts', inline=False)
        embedo.add_field(value='eeeeh', name='Mcbot are u gay?', inline=False)
        embedo.add_field(value='Ok then', name='Mcbot pls say something', inline=False)
        embedo.add_field(value='Stooop!', name='Mcbot say something else', inline=False)
        embedo.add_field(value='Basic kindergarten 1 to 10', name='Mcbot Countdown from 10', inline=False)
        embedo.add_field(value='Never gonna give you up', name='Mcbot pls rickroll me', inline=False)
        embedo.add_field(value='Nothing much', name='Mcbot what are you thinkking?', inline=False)
        embedo.add_field(value='It is just a pun, cmon dont cringe', name='Mcbot say something about life', inline=False)

        await message.channel.send(embed=embedo)

    elif "mcbot countdown from 10" in message.content.lower():
        await message.channel.send("10...")
        await message.channel.send("9...")
        await message.channel.send("8...")
        await message.channel.send("7...")
        await message.channel.send("6...")
        await message.channel.send("5...")
        await message.channel.send("4...")
        await message.channel.send("3...")
        await message.channel.send("2...")
        await message.channel.send("1 Run!")

    elif "mcbot send something funny" in message.content.lower():
        bruhd = discord.Embed(
            title = 'Non randomized Something Funny',
            description = 'Bruh moment',
        )

        bruhd.set_footer(text='Powered by some shitty code')
        bruhd.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        bruhd.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        bruhd.set_image(url='https://cdn.discordapp.com/attachments/654414431731580965/725328280244322314/t2z7txxozt651.png')
        
        await message.channel.send(embed=bruhd)



    elif "mcbot pls say something" in message.content.lower():
        await message.channel.send("Ok!")
        await message.channel.send("Did you know that bananas are radioactive?")

    elif "mcbot >>>addresslook google.com" in message.content.lower():
        await message.channel.send("Go to cmd and type `nslookup google.com`")

    elif "mcbot say something else" in message.content.lower():
        await message.channel.send("Fine!")
        await message.channel.send("https://www.youtube.com/watch?v=rfscVS0vtbw")
        await message.channel.send("Here's some coding tutorial for you dummies!")
        await message.channel.send("Annoying Humans!")

    elif "shut up mcbot!" in message.content.lower():
        await message.channel.send("No you shut up! You Annoying Humans!")

    elif "mcbot pls prompt commands" in message.content.lower():
        haks = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.green()
        )

        haks.set_footer(text='Powered by some shitty code')
        haks.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        haks.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        haks.add_field(value='Checks ping in ms', name='Mcbot >>>ping latency test')
        haks.add_field(value='windows_xp_shutdown.mp3', name='Mcbot >>>kill', inline=False)
        haks.add_field(value='Is this illegal?', name='Mcbot >>>addresslookup google.com', inline=False)
        haks.add_field(value='Same as Source code unofficial server id!', name='Mcbot >>>fanmclainebot unofficial sever id', inline=False)


        await message.channel.send(embed=haks)


    elif "mcbot >>>kill" in message.content.lower():
        await message.channel.send("You can't just shutdown me like that!")

    elif "mcbot pls give me a python tutorial" in message.content.lower():
        await message.channel.send("Here's some python tutorial: https://www.youtube.com/watch?v=rfscVS0vtbw")


    elif "mcbot pls rickroll me" in message.content.lower():
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif "mcbot what are you thinking?" in message.content.lower():
        await message.channel.send("https://www.youtube.com/watch?v=SDTZ7iX4vTQ")
        await message.channel.send("RUN!!")

    elif "let me inn" in message.content.lower():
        await message.channel.send("Let me in! https://tenor.com/5LZw.gif ")

    elif "bruhh" in message.content.lower():
        await message.channel.send("bruh https://tenor.com/zYmf.gif ")

    elif "nothing mcbot" in message.content.lower():
        await message.channel.send("Don't say nothing, say everything c'mon don't be shy, I'm here supporting you!")

    elif "hey mcbot! wanna say something to me?" in message.content.lower():
        await message.channel.send("Yeah!")
        await message.channel.send("Creator, If you live to be 100, I hope I live to be 100 minus 1 day, so I never have to live without you. : D")

    elif "im bacc" in message.content.lower():
        await message.channel.send("Hi bacc, i am FanMclaineBot AKA Mcbot")

    elif "ok bot" in message.content.lower():
        await message.channel.send("Ok boomer!")

    elif "say something wholesome pls!, i need support" in message.content.lower():
        await message.channel.send("Don't woory im supporting you even if i am gone ; )")

    elif "say something about friends mcbot" in message.content.lower():
        await message.channel.send("The happiest people don’t have the best of everything, they just make the best of everything. :)")

    #social media commands

    elif "mcbot pls social media commands" in message.content.lower():
        sweet = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.blue()
        )

        sweet.set_footer(text='Powered by some shitty code')
        sweet.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        sweet.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        sweet.add_field(value='Sends a link to youtube', name='Mcbot pls open youtube', inline=False)
        sweet.add_field(value='Sends a link to reddit', name='Mcbot pls open reddit', inline=False)
        sweet.add_field(value='Gives a coding tutorial', name='Mcbot pls give me a C# tutorial/ Python tutorial', inline=False)

        await message.channel.send(embed=sweet)

    elif "mcbot pls open youtube" in message.content.lower():
        await message.channel.send("Youtbe: https://www.youtube.com/ ")

    elif "mcbot pls open reddit" in message.content.lower():
        await message.channel.send("Reddit: https://www.reddit.com/")

    elif "mcbot pls give me a c# tutorial" in message.content.lower():
        await message.channel.send("Here's some C# tutorial: https://www.youtube.com/watch?v=GhQdlIFylQ8")  
    
    #nsfw

    elif "mcbot pls nsfw commands" in message.content.lower():
        leny = discord.Embed(
            title = 'Commands',
            description = 'Some commands may not work',
            colour = discord.Colour.purple()
        )

        leny.set_footer(text='Powered by some shitty code')
        leny.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        leny.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        leny.add_field(value='Pls no', name='nsfw mcbot')
        leny.add_field(value='This post right here officer', name='Mcbot say a nsfw joke', inline=False)
        
        await message.channel.send(embed=leny)


    elif "nsfw mcbot" in message.content.lower():
        await message.channel.send(" Wha- What are you doing step-human?")

    elif "mcbot say a nsfw joke" in message.content.lower():
        bruh = discord.Embed(
            title = 'Nsfw joke',
            description = 'Why do KFC have no toilet paper? Because it is **Finger Licking Good**'
        )

        bruh.set_footer(text='Powered by some shitty code')
        bruh.set_thumbnail(url='https://cdn.discordapp.com/attachments/709477782828220451/725687256836341800/discord_bot_pfp.jpg')
        bruh.set_author(name='Fanmclaine1109', icon_url='https://cdn.discordapp.com/attachments/718492380051013667/725947993316130816/3a9a2446a2a0675a0b21c472b95f555893bcbba7.png')
        bruh.set_image(url='https://www.pngmart.com/files/11/LMAO-Emoji-PNG-File.png')
        
        await message.channel.send(embed=bruh)


    #admin commands
     

client.run("Hehe boi")
Run = "Run"

Example_string = "dont worry mcbot will support you on everything"
Source_cODE_Server_Id = "709477782828220446"
FanMclaineBot_Server_id = "718492380051013663"


