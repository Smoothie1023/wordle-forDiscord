import discord
import random
from discord.ui import Button,View
from discord.commands import Option

bot=discord.Bot()
guild_id=open('guild_id.txt','r',encoding='UTF-8').read()[:-1]

class wordle:
    def __init__(self):
        words=open('wordlist.txt','r',encoding='UTF-8').read().split()
        select=random.randint(0,len(words)-1)
        self.time=0
        self.word=words[select]
        print(self.word)

    def input_word(self,input):
        self.correct=[]
        self.exist=[]
        #位置文字ともに正解か判定
        for i in range(5):
            if(self.word[i]==input[i]):
                self.correct.append(i)
        #位置が正解か判定
        for w in self.word:
            for i in range(5):
                if(w==input[i]):
                    self.exist.append(i)

@bot.event
async def on_ready():
    print('Raedy...')

@bot.slash_command(guild_ids=[guild_id],description='wordleを開始')
async def start(ctx):
    global Game
    Game=wordle()
    view=View()

    for i in range(5):
        view.add_item(discord.ui.Button(disabled=True,label=' ',style=discord.ButtonStyle.gray))
    await ctx.respond('ゲームを開始しました',view=view)

@bot.slash_command(guild_ids=[guild_id],description='回答＊要/startコマンド')
async def answer(
    ctx,
    ans:Option(str,'任意の５文字を入力してください')
):
    global Game
    view=View()
    gray=discord.ButtonStyle.gray   #gray:合っていない
    green=discord.ButtonStyle.green #green:位置文字共に合っている
    red=discord.ButtonStyle.red     #red:文字は含まれるが位置が違う
    styles=[gray,gray,gray,gray,gray]

    if(len(ans)!=5):
        await ctx.respond('5文字入力してください')
        return
    try:
        Game.input_word(ans)
    except:
        await ctx.respond('/startをしてゲームを開始してください')
        return
    #input_wordより得た結果をリストに格納
    for exist in Game.exist:styles[exist]=red
    for correct in Game.correct:styles[correct]=green
    #Viewにボタンを追加
    for i in range(5):
        view.add_item(discord.ui.Button(disabled=True,label=ans[i],style=styles[i]))
    #結果表示
    Game.time=Game.time+1
    await ctx.respond('結果 '+str(Game.time)+'/6',view=view)
    #クリアor失敗判定
    if(len(Game.correct)==5):
        await ctx.respond('クリア')
        del Game
        return
    if(Game.time==6):
        await ctx.respond('失敗 答え:'+Game.word)
        del Game
        return

@bot.slash_command(guild_ids=[guild_id],description="ゲームを中断")
async def kill(ctx):
    global Game
    try:
        del Game
        await ctx.respond('ゲームを中断しました')
    except:
        await ctx.respond('ゲームは開始されていません')

token=open('token.txt','r',encoding='UTF-8').read()[:-1]
bot.run(token)
