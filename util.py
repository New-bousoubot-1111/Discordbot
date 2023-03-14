import nextcord
import json

with open('json/config.json','r') as f:
	config = json.load(f)
with open('json/help.json','r') as f:
	help = json.load(f)

color = nextcord.Colour(int(config['color'],16))

#ページボタン
class page_button(nextcord.ui.View):
  def __init__(self,embed,embed2):
    super().__init__(timeout=None)
    self.value = None
    self.embed = embed
    self.embed2 = embed2

  @nextcord.ui.button(label="情報",style=nextcord.ButtonStyle.green)
  async def close_the_error(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
    await interaction.response.edit_message(embed=self.embed)

  @nextcord.ui.button(label="コマンド",style=nextcord.ButtonStyle.green)
  async def open_the_error(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
    await interaction.response.edit_message(embed=self.embed2)
    
#管理者
def creator_only():
  embed=nextcord.Embed(title="Error",description="このコマンドは管理者専用です",color=0xff0000)
  return embed
