import discord
import os
import random
import asyncio
import asyncpraw
import time
from discord import Client, Intents, Embed
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from dotenv import load_dotenv
from youtube_dl import YoutubeDL
from time import sleep

intents = discord.Intents.all()

agent='furry_irl')

intents.members = False

load_dotenv()
client = commands.Bot(command_prefix=['lfs! ','lfs!'], intents=Intents.all())

client.remove_command('help')

client.remove_command('lovetest')
#--------------------------------------------------------------Furry Security bot---------------------------------------------------------------------------


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Protecting the furs!'))
    print('Bot is online')


role = "------Member----"


@client.event
async def on_member_join(member):
    welcomes = [f'**{member.mention}** just got summoned in Le Furry Hideout',
                f'**{member.mention}** got here thorugh a Transfur!',
                f'Welcome to the best Furry Server **{member.mention}**!']

    ch = client.get_channel(838849651725565993)
    await ch.send(f'{random.choice(welcomes)}!')

@client.command()
async def ping(ctx):
    print('Ping was used')
    await ctx.send(f'Bot ping: {round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(
        title='Commands for Furs :3 \n \nPrefix: lfs! \n \nFun Commands: \nfuncmd \n \nReddit Commands(CURRENTLY UNAVAILABLE): \nredcmd \n \nInteraction: \nintcmd \n \nMod commands: \nmodcmd \n \nUseful commands: \nusecmd \n \nMusic Commands (**NEW**): \nmuscmd',
        color=discord.Color.green())
    await ctx.send(embed=embed)


@client.command()
async def funcmd(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(
        title='Fun Commands: \n \n8ball (Question) \nCoin \nDice \nLovetest (someone) \nGayrate \nsimprate',
        color=discord.Color.green())
    await ctx.send(embed=embed)
    
@client.command()
async def redcmd(ctx):
    print('unv was used')
    embed = discord.Embed(
        title='CURRENTLY UNAVAILABLE',
        color=discord.Color.red())
    await ctx.send(embed=embed)

#@client.command()
#async def redcmd(ctx):
#    print('cmdhelp was used')
#    embed = discord.Embed(
#        title='Fun Commands: \n \nmeme (sends a r/memes meme) \nfurmeme (sends a r/furry meme) \nmeme_irl (sends a r/furry_irl meme)',
#        color=discord.Color.green())
#    await ctx.send(embed=embed)
    
@client.command()
async def intcmd(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(
        title='Interactive Commands: \n \nhug (someone) \nkiss (someone) \npat (someone)',
        color=discord.Color.green())
    await ctx.send(embed=embed)
    
@client.command()
async def muscmd(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(
        title='Music commands: \n \nplay (URL) \npause \nresume \nstop \nleave',
        color=discord.Color.green())
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def modcmd(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(title='Mod Commands: \n \nKick (User) \nBan (User) \nClear (amount) \nUnban (User)',
                          color=discord.Color.green())
    await ctx.send(embed=embed)
    
@client.command()
async def usecmd(ctx):
    print('cmdhelp was used')
    embed = discord.Embed(title='Useful Commands: \n \nMath: \nPlus (num1) (num2) \nMinus (num1) (num2) \nMult (num1) (num2) \nDiv (num1) (num2)',
                          color=discord.Color.green())
    await ctx.send(embed=embed)


@client.command(aliases=['8ball', 'eightball'])
@commands.cooldown(rate=1, per=5)
async def _8ball(ctx, *, question):
    print('8ball was used')
    responses = ['It is certain',
                 'It is decidedly so',
                 'Without a doubt',
                 'Yes – definitely',
                 'You may rely on it',
                 'As I see it, yes',
                 'Most likely',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes',
                 'Reply hazy, try again',
                 'Ask again later',
                 'Better not tell you now',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'My reply is no',
                 'My sources say no',
                 'Outlook not so good',
                 'Very doubtful']
    embed = discord.Embed(title=f'Question: {question}\nAnswer: {random.choice(responses)}',
                          color=discord.Color.blue())
    await ctx.send(embed=embed)
    
#Calculator
@client.command()
async def plus(ctx, num, num2):
    print('plus was used')
    ans = f'{float(num) + float(num2)}'

    await ctx.send(f'{ans}')
    
@client.command()
async def minus(ctx, num, num2):
    print('plus was used')
    ans = f'{float(num) - float(num2)}'

    await ctx.send(f'{ans}')
    
@client.command()
async def mult(ctx, num, num2):
    print('plus was used')
    ans = f'{float(num) * float(num2)}'

    await ctx.send(f'{ans}')

@client.command()
async def div(ctx, num, num2):
    print('plus was used')
    ans = f'{float(num) / float(num2)}'

    await ctx.send(f'{ans}')

@client.command(aliases=['lover8', 'lovetest', '<3test'])
@commands.cooldown(rate=1, per=5)
async def _lover8(ctx, *, question):
    author_name = ctx.message.author.name
    print('lovetest was used')
    prc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    await ctx.send(f'The love between {author_name} and {question} is {random.choice(prc1)}%')

@client.command(aliases=['gayr8', 'gayrate'])
@commands.cooldown(rate=1, per=5)
async def _gayr8(ctx):
    author_name = ctx.message.author.name
    print('gayrate was used')
    prc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    embed = discord.Embed(title=f'{author_name} is {random.choice(prc1)}% gay',
                          color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@client.command(aliases=['simpr8', 'simprate'])
@commands.cooldown(rate=1, per=5)
async def _simpr8(ctx):
    author_name = ctx.message.author.name
    print('simprate was used')
    prc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    embed = discord.Embed(title=f'{author_name} is {random.choice(prc1)}% a simp',
                          color=discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(rate=1, per=5)
async def dice(ctx):
    print('Dice was used')
    dice = ['1',
            '2',
            '3',
            '4',
            '5',
            '6']
    embed = discord.Embed(title=f'You rolled a {random.choice(dice)}!',
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(rate=1, per=5)
async def coin(ctx):
    print('Coin was used')
    rollcn = ['Heads',
              'Tails']
    embed = discord.Embed(title=f'Your coin landed on {random.choice(rollcn)}!',
                          color=discord.Color.blue())
    await ctx.send(embed=embed)
    
#---------------------------------------Music----------------------------------------

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def play(ctx, url):
    global queue
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()  
        
        embed = discord.Embed(title=f'Bot is playing {url}',
                              color=discord.Color.blue()
                             )
        
        await ctx.send(embed=embed)

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return
    
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')
        
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')
        
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')
        
@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.guild.voice_client
	await server.disconnect()
        
#-------------------------------------------------------------------------------
    
@client.command()
async def meme_irl(ctx):
    memes_submissions = reddit.subreddit('furry_irl').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Meme requested by {ctx.author}', description=f'**IF NSFW INCLUDED DELETE IMMEDIATELY!** \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)
    
@client.command()
async def furmeme(ctx):
    memes_submissions = reddit.subreddit('furry').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Meme requested by {ctx.author}', description=f'**IF NSFW INCLUDED DELETE IMMEDIATELY!** \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)
    
@client.command()
async def meme(ctx):
    meme_subreddit = await reddit.subreddit('memes')
    memes_submissions = meme_subreddit.hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Meme requested by {ctx.author}', description=f'**IF NSFW INCLUDED DELETE IMMEDIATELY!** \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)
    
@client.command()
@commands.is_nsfw()
async def furpussy(ctx):
    memes_submissions = reddit.subreddit('furrypussy').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Meme requested by {ctx.author}', description=f'**NSFW WARNING!!!** \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)
    
@client.command()
@commands.is_nsfw()
async def furpenis(ctx):
    memes_submissions = reddit.subreddit('DragonPenis').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Meme requested by {ctx.author}', description=f'**NSFW WARNING!!!** \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)
    
@client.command()
@commands.is_nsfw()
async def yiff(ctx):
    memes_submissions = reddit.subreddit('yiff').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        
    e = discord.Embed(title=f'Yiff requested by {ctx.author} \nDesc: {submission.title}', color=0x1F)
    e.set_image(url=submission.url)
 
    await ctx.send(embed=e)

@client.command()
async def hug(ctx, *, member):
    author_name = ctx.message.author.name
    hugs = [f'**{author_name}** warmly cuddles {member}!',
            f"**{author_name}** hugs {member} like they're their boyfriend!",
            f'**{author_name}** Runs to {member} and cuddles them as hard as possible!',
            f'**{author_name}** wraps around {member} and hugs them!',
            f'**{author_name}** looks at {member} and just gives them the biggest hug ever!!!']

    await ctx.send(f'{random.choice(hugs)}')


@client.command()
async def kiss(ctx, *, member):
    author_name = ctx.message.author.name
    kiss = [f'**{author_name}** goes near {member} and kisses them!',
            f'**{author_name}** kisses {member}!',
            f'**{author_name}** runs to {member} and kisses them as hard as possible!',
            f'**{author_name}** pushes {member} against a wall and kisses them!',
            f'**{author_name}** looks at {member} and just gives them the biggest kiss ever!!!']

    await ctx.send(f'{random.choice(kiss)}')
    
@client.command()
async def pat(ctx, *, member):
    author_name = ctx.message.author.name
    pats = [f'**{author_name}** goes near {member} and pats em!',
            f'**{author_name}** pats {member}!',
            f'**{author_name}** gives {member} a magical pat!',
            f'**{author_name}** gave {member} a pat through the screen!']

    await ctx.send(f'{random.choice(pats)}')

@client.event
async def on_command_error(ctx, error):
    print('Command_Error')
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Command doesn't exist or is written wrong",
                              color=discord.Color.red())
        await ctx.send(embed=embed, delete_after=5)
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f"This command is on cooldown, try again after {round(error.retry_after)}s",
                              color=discord.Color.red())
        await ctx.send(embed=embed, delete_after=5)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Insufficient Permissions",
                              color=discord.Color.red())
        await ctx.send(embed=embed, delete_after=5)
    if isinstance(error, commands.NSFWChannelRequired):
        embed = discord.Embed(title="Command only for NSFW Channels!",
                              color=discord.Color.red())
        await ctx.send(embed=embed, delete_after=5)

@client.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount: int):
    print('Clear was used')
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Cleared {amount} Messages!', delete_after=5)


@clear.error
async def clear_error(ctx, error):
    print('Clear_Error')
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='Please specify an amount of messages to delete',
                              color=discord.Color.red())
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return
