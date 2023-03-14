import requests
import json
from replit import db
import os
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
  #main.py update
  with open('json/version.txt','w') as f:
    f.write(new_version)
  with open('main.py','w') as f:
    mainpy = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/main.py").text
    f.write(mainpy)
  #config.json update
  with open('json/new.json','w') as f:
    new_json = requests.get("https://raw.githubusercontent.com/New-bousoubot-1111/Discordbot/main/json/help.json").json()
    json.dump(new_json,f,indent=4)

  with open('json/help.json','r') as f:
    config = json.load(f)

  for i in config:
    db[i] = str(config[i])

  with open('json/new.json','r') as f:
    new = json.load(f)
  with open('json/help.json','w') as f:
    json.dump(new,f,indent=4)
  
  for i in db.keys():
    with open('json/help.json','r') as f:
      config = json.load(f)
      config[i] = str(db[i])
      del db[i]
    with open('json/help.json','w') as f:
      json.dump(config,f,indent=4)
  os.remove("json/new.json")
  print(Fore.GREEN + "アップデートが完了しました" + Fore.RESET)
else:
  print(Fore.GREEN + "アップデートはありませんでした" + Fore.RESET)