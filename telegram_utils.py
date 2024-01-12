import telegram


async def send_telegram(photo_path="alert.png"):
    try:
        my_token = "YOUR_TOKEN"
        bot = telegram.Bot(token=my_token)
        await bot.send_photo(chat_id=YOUR_CHAT_ID, photo=open(photo_path, "rb"), caption="Intrusion, Danger!")
    except Exception as ex:
        print("Cannot send telegram message:", ex)

    print("Send success")

# Create an event loop and run the function asynchronously
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(send_telegram())
