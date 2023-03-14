import requests
from colorama import Fore

print(Fore.GREEN + "アップデートを確認しています" + Fore.RESET)
with open('README.md','w') as f:
  README = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/README.md").text
  f.write(README)

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
    with open('main.py','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/main.py").text
      f.write(new_code)
  #util.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('util.py','w') as f:
    with open('util.py','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/util.py").text
      f.write(new_code)
  #update.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('update.py','w') as f:
    updatepy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/update.py").text
    f.write(updatepy)
  #adimin.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/admin.py','w') as f:
    with open('modules/admin.py','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/admin.py").text
      f.write(new_code)
  #command.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/command.py','w') as f:
    with open('modules/command.py','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/command.py").text
      f.write(new_code)
  #tasks.py
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('modules/tasks.py','w') as f:
    with open('modules/tasks.py','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/modules/tasks.py").text
      f.write(new_code)
  #config.json
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('json/config.json','w') as f:
    with open('json/config.json','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/config.json").text
      f.write(new_code)
  #help.json
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('json/help.json','w') as f:
    with open('json/help.json','r') as f:
      new_code = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/help.json").text
      f.write(new_code)
