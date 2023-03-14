import requests
from colorama import Fore

print(Fore.GREEN + "アップデートを確認しています" + Fore.RESET)
with open('LICENSE','w') as f:
  license = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/LICENSE").text
  f.write(license)

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
    configjson = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/main.py").text
    f.write(configjson)
  #help.json
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('json/help.json','w') as f:
    helpjson = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/main.py").text
    f.write(helpjson)
  print(Fore.GREEN + "アップデートが完了しました" + Fore.RESET)
else:
  print(Fore.GREEN + "アップデートはありませんでした" + Fore.RESET)
