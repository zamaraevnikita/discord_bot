import conf
import discord

client = discord.Client()

@client.event
async def on_message(message):
    # <Message id=825338401469366313 channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539>
    #  type=<MessageType.default: 0>
    #  author=<Member id=424521921074429953 name='♿MERU☭' discriminator='6218' bot=False nick='♿Никита☭' guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
    #  flags=<MessageFlags value=0>>


    if message.author == client.user:
        return
    

    if message.author.bot:
        return

    if message.author == client.user:
        return
    
    #задаём каналы для бота
    if message.channel.id == 825309543427866625:
        # изначально msg пустое
        msg = None 

        # ответ пользователю в формате " hallo  {user name} - your message {user.content}"
        

        # сообщение с методом send



        #1. /hello - сообщение
        #2. /about_me сообщение пользователю по его параметрам id/name (если есть ник, то добавить ник "твой nick")
        #3 /repeat [] - повторить за пользователем

        if message.content == "/repeat":
            msg = f'{message.content} '
        elif message.content == "/about_me":
            msg = f' your id - {message.author.id},'
            if message.author.nick:
                msg = f'your id - {message.author.id}, your nick - {message.author.nick},'
        if message.content == "/hello":
            msg = f'hello '





        await message.channel.send(msg)







client.run(conf.bot_token)
