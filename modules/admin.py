import nextcord
from nextcord.ext import commands
from colorama import Fore
import json

with open('json/channel.json','r') as r:
  load = json.load(r)

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
  
    @commands.Cog.listener()
    async def on_ready(self):
      print(Fore.BLUE + "|admin         |" + Fore.RESET)

    #登録されたチャンネルにお知らせを送信する
    @commands.command()
    async def notice(self, ctx, args=None, args2=None):
        if args == None:
            em = nextcord.Embed(title="Error",description="タイトルを書いてください",color=0xff0000)
            await ctx.send(embed=em)
        if args2 == None:
            em = nextcord.Embed(title="Error",description="内容を書いてください",color=0xff0000)
            await ctx.send(embed=em)
        else:
            if ctx.author.guild_permissions.administrator:
              for guild in load:
                em=nextcord.Embed(title=args, description=args2,color=0x08e2b7)
              channel = self.bot.get_channel(int(load[guild]))
              await channel.send(embed=em)
            else:
              em=nextcord.Embed(title="Error", description="このコマンドは管理者専用です",color=0xff0000)
              await ctx.send(embed=em)
      
    #メッセージ削除
    @commands.command()
    async def clear(self, ctx, amount : int=None):
        if amount == None:
            em = nextcord.Embed(title="Error",description="数値を指定してください。",color=0xff0000)
            await ctx.send(embed=em)
        else:
            if ctx.author.guild_permissions.administrator:
                await ctx.channel.purge(limit=amount)
                em=nextcord.Embed(title="削除", description=f"{amount}件のメッセージを削除しました",color=0x08e2b7)
                await ctx.send(embed=em)
            else:
                em=nextcord.Embed(title="Error", description="このコマンドは管理者専用です",color=0xff0000)
                await ctx.send(embed=em)
    @commands.command()
    async def clear_all(self, ctx):
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=None)
            em=nextcord.Embed(title="削除", description="全てのメッセージを削除しました",color=0x08e2b7)
            await ctx.send(embed=em)
        else:
            em=nextcord.Embed(title="Error", description="このコマンドは管理者専用です",color=0xff0000)
            await ctx.send(embed=em)

    #キック
    @commands.command()
    async def kick(self, ctx,member :  nextcord.Member=None, *, reason=None):
        if member == None:
            em = nextcord.Embed(title="Error",description="メンバーを指定してください",color=0xff0000)
            await ctx.send(embed=em)
        else:
            if ctx.author.guild_permissions.administrator:
                await member.kick(reason=reason)
                em=nextcord.Embed(title=f'{member}をサーバーからkickしました',color=0x08e2b7)
                em.add_field(name=f'理由',value=reason)
                await ctx.send(embed=em)
            else:
                em=nextcord.Embed(title="Error", description="このコマンドは管理者専用です。",color=0xff0000)
                await ctx.send(embed=em)

    #バン
    @commands.command()
    async def ban(self, ctx, member : nextcord.Member=None, *, reason=None):
        if member == None:
            em = nextcord.Embed(title="Error",description="メンバーを指定してください",color=0xff0000)
            await ctx.send(embed=em)
        else:
            if ctx.author.guild_permissions.administrator:
                await member.ban(reason=reason)
                em=nextcord.Embed(title=f'{member}をサーバーからbanしました',color=0x08e2b7)
                em.add_field(name=f'理由',value=reason)
                await ctx.send(embed=em)
            else:
                em=nextcord.Embed(title="Error", description="このコマンドは管理者専用です",color=0xff0000)
                await ctx.send(embed=em)



def setup(bot):
    return bot.add_cog(admin(bot))
