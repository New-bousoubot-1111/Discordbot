import nextcord
from nextcord.ext import commands
import Levenshtein
import json
from colorama import Fore
import os
import webserver

with open('json/config.json', 'r') as f:
    config = json.load(f)

intents = nextcord.Intents.all()
bot = commands.Bot(
	command_prefix=config['prefix'],
	help_command=None
)
for module in config['modules']:
    bot.load_extension(f"modules.{module}")

#起動時のログ
@bot.event
async def on_ready():
    print(Fore.GREEN + f"[Ready]\nbot:{bot.user.name}" + Fore.RESET)
    print(Fore.BLUE + "読み込みファイル" + Fore.RESET)
    print(Fore.BLUE + "----------------" + Fore.RESET)

#エラー処理
@bot.event
async def on_command_error(ctx, error:Exception):
    if isinstance(error, commands.errors.CommandNotFound):
        body = ctx.message.content.lstrip(ctx.prefix)
        res = []
        for i in bot.commands:
            check = Levenshtein.distance(str(i), str(body))
            if check <= 2:
                res.append(str(i))
        embed = nextcord.Embed(title="Error",
                               description=f"コマンドが見つかりません",
                               color=0xff0000)
        if not res == []:
            suggest = "".join([f'`{x}`\n' for x in res])
            embed.add_field(name="もしかして...", value=suggest)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.NotOwner):
        em = nextcord.Embed(title="このコマンドは使用できません",
                            description="このコマンドは管理者専用です",
                            color=0xff0000)
        await ctx.send(embed=em)
    else:
        embed=nextcord.Embed(title="エラーが発生しました",description=f"Error ID:`{ctx.message.id}`\n```py\n{error}\n```",color=0xff0000)
        await ctx.channel.send(embed=embed)

webserver.start()
try:
    bot.run(os.getenv("token"))
except:
    os.system("kill 1")