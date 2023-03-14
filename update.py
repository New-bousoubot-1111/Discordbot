import requests
from colorama import Fore

print(Fore.GREEN + "アップデートを確認しています" + Fore.RESET)
with open('README.md','r') as f:
  now_readme = f.read()
  new_readme = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/README.md").text
  f.write(new_readme)

if now_README != new_README:
  print(Fore.GREEN + f"READMEの更新を確認しました" + Fore.RESET)
  print(Fore.GREEN + "READMEを更新中です" + Fore.RESET)
  print(Fore.GREEN + "READMEの更新が完了しました" + Fore.RESET)

with open('json/version.txt','r') as f:
  now_version = f.read()
new_version = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/version.txt").text

if now_version != new_version:
  print(Fore.GREEN + f"バージョン{new_version}へのアップデートを確認しました" + Fore.RESET)
  print(Fore.GREEN + "アップデートを適応中です" + Fore.RESET)
  #main.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('main.py','w') as f:
    mainpy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/main.py").text
    f.write(mainpy)
  #util.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('util.py','w') as f:
    utilpy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/util.py").text
    f.write(utilpy)
  #update.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('update.py','w') as f:
    updatepy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/update.py").text
    f.write(updatepy)
  #admin.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/admin.py','w') as f:
    adminpy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/admin.py").text
    f.write(adminpy)
  #command.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/command.py','w') as f:
    commandpy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/command.py").text
    f.write(commandpy)
  #tasks.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/tasks.py','w') as f:
    taskspy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/tasks.py").text
    f.write(taskspy)
  #config.json
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('json/config.json','w') as f:
    configjson = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/config.json").text
    f.write(configjson)
  #help.json
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('json/help.json','w') as f:
    helpjson = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/help.json").text
    f.write(helpjson)
  print(Fore.GREEN + "アップデートが完了しました" + Fore.RESET)
else:
  print(Fore.GREEN + "アップデートはありませんでした" + Fore.RESET)
