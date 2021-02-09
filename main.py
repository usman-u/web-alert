from discord_webhook import DiscordWebhook




in_stock = False




def discord(msg):
	
	webhook = DiscordWebhook(url='https://discord.com/api/webhooks/808829261666189312/ErkuQx7hoUe-RxC6Og8j1dxpv15x3AAVk4HJB1i96aNP9pCWSUsQAHfaLa0Q0wSKhfu8', content=msg)
	response = webhook.execute()


if in_stock == True:
		
	msg = "In Stock @F2ncy"
	discord(msg)

if in_stock == False:
	msg = "Not In stock"
	discord(msg)





