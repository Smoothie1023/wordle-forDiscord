import discord
import random
from discord.ui import Button,View
from discord.commands import Option


bot=discord.Bot()
guild_id=open('guild_id.txt','r',encoding='UTF-8').read()[:-1]

global Game

class wordle:
    def __init__(self):
        words=open('wordlist.txt','r',encoding='UTF-8').read().split()
        select=random.randint(0,len(words))
        self.word=words[select]
        print(self.word)
    def input_word(self,input):
        self.correct=[]
        self.exist=[]
        for i in range(5):
            if(self.word[i]==input[i]):
                self.correct.append(i)
        for w in self.word:
            for i in range(5):
                if(w==input[i]):
                    self.exist.append(i)
        self.correct.sort()
        self.exist.sort()
        print(self.exist)

@bot.event
async def on_ready():
    print("Raedy...")

@bot.slash_command(guild_ids=[guild_id],description="wordleを開始する。")
async def start(ctx):
    global Game
    Game=wordle()
    view=View()
    for i in range(5):
        view.add_item(discord.ui.Button(disabled=True,label=' ',style=discord.ButtonStyle.gray))
    await ctx.respond('ゲームを開始しました。',view=view)


@bot.slash_command(guild_ids=[guild_id],description="回答する*要startコマンド")
async def answer(
    ctx,
    ans:Option(str,'任意の５文字を入力してください')
):
    if(len(ans)!=5):
        await ctx.respond('5文字入力してください')
        return

    global Game
    try:
        Game.input_word(ans)
    except:
        await ctx.respond('/startをしてゲームを開始してください')
        return

    gray=discord.ButtonStyle.gray
    green=discord.ButtonStyle.green
    red=discord.ButtonStyle.red
    #gray:合っていない
    #green:位置文字共に合っている
    #red:文字は含まれるが位置が違う
    styles=[gray,gray,gray,gray,gray]
    for exist in Game.exist:styles[exist]=red
    for correct in Game.correct:styles[correct]=green
    view=View()
    for i in range(5):
        view.add_item(discord.ui.Button(disabled=True,label=ans[i],style=styles[i]))
    await ctx.respond('結果',view=view)
    if(len(Game.correct)==5):
        await ctx.respond('クリア')
        del Game

token=open('token.txt','r',encoding='UTF-8').read()[:-1]
bot.run(token)
