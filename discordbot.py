import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("똥싸는 중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("그래 안뇽")

client.run("Nzk1Nzg3MjIwNzQwODY2MDg4.X_Ocmg.nbjSz3hPWsDkbwwv2v-pTMhMNz0")



