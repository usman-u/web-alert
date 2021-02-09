from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/808829261666189312/ErkuQx7hoUe-RxC6Og8j1dxpv15x3AAVk4HJB1i96aNP9pCWSUsQAHfaLa0Q0wSKhfu8', content='Webhook Message')
response = webhook.execute()
