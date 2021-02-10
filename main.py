from discord_webhook import DiscordWebhook
from time import ctime
from bs4 import BeautifulSoup
import requests

URL = "https://www.awd-it.co.uk/xfx-gts-radeon-rx-580-8gb-xxx-gddr5-pci-express-gaming-graphics-card.html"
page = requests.get(URL, headers = {'User-agent': 'Super Bot Power Level Over 9000'})

soup = BeautifulSoup(page.content, 'html.parser')

string = str(soup)

if 'OutOfStock' in string:
	print("OutOfStock") 
	in_stock = False
if "InStock" in string:
	print ("instock")
	in_stock = True

time = ctime()
def discord(msg):
	webhook = DiscordWebhook(url='https://discord.com/api/webhooks/808829261666189312/ErkuQx7hoUe-RxC6Og8j1dxpv15x3AAVk4HJB1i96aNP9pCWSUsQAHfaLa0Q0wSKhfu8', content=msg)
	response = webhook.execute()  # executes webhook

if in_stock == True:
		
	msg = "`In Stock` @F2ncy ! "
	discord(msg + time)
	print ("In Stock " + time)
	

if in_stock == False:
	msg = "`Not In stock` "
	discord(msg + time)
	print ("Out of Stock " + time)




