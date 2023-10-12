from logging import error

from pyrogram import Client
from pyrogram.filters import chat

from config import API_ID, API_HASH, CHANNELS_ID_LIST, CHANNELS_MESSAGE_LIST

# Create a Pyrogram client
app = Client("Personal Account", API_ID, API_HASH)


async def send_comment(channel_id, message_id, text):
    """
    Send a comment to a specific message in a channel.

    Args:
        channel_id (int): The ID of the group for comment.
        message_id (int): The ID of the message to reply to.
        text (str): The text of the comment.
    """
    try:
        discussion_message = await app.get_discussion_message(channel_id, message_id)
        await discussion_message.reply(text)
    except Exception as e:
        # Log the error to the error.log file
        error(f"Error sending comment: {str(e)}")


@app.on_message(chat(CHANNELS_ID_LIST[0]))
async def new_message_handler(client, message):
    """
    Handle new messages in channels and send comments.
    """
    await send_comment(CHANNELS_ID_LIST[0], message.id, CHANNELS_MESSAGE_LIST[0])


if __name__ == "__main__":
    app.run()
