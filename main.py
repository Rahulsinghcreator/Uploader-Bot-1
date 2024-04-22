import threading
import requests
from telegram.ext import Updater, CommandHandler

# Define the function to download a link
def download_link(url):
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as file:
            file.write(response.content)
        return f"Downloaded {filename} successfully!"
    else:
        return "Failed to download link."

# Define the function to handle the /download command
def download(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Please provide a link to download.")
        return

    link = context.args[0]
    update.message.reply_text(download_link(link))

# Define the function to handle the /upload command
def upload(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Please provide a filename to upload.")
        return

    filename = context.args[0]
    with open(filename, 'rb') as file:
        context.bot.send_document(update.message.chat_id, document=file)

# Define the main function to start the bot
def main():
    # Initialize the bot
    updater = Updater("6874298081:AAFolEJq4zqyJORJuENjXpOsWCi5R91oTZA", use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("download", download))
    dispatcher.add_handler(CommandHandler("upload", upload))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
