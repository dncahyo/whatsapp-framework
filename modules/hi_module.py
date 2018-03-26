# modules/hi_module.py

from app.mac import mac, signals
from modules import ron_quotes

@signals.message_received.connect
def handle(message):
    #message.log() to see message object properties
    if message.text == "hello":
        mac.send_message("Hello " + message.who_name, message.conversation)
        #mac.send_image("path/to/image.png", message.conversation)
        #mac.send_video("path/to/video.mp4", message.conversation)
    elif message.text == "cahyo":
        mac.send_message("kumolo", message.conversation)
    elif message.text == "quotes":
        mac.send_message(ron_quotes.get_quote(), message.conversation)
