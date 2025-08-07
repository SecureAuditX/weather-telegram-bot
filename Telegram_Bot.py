
# Telegram Weather Logic
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram import Update
from Config import TELEGRAM_BOT_TOKEN        # Your bot token
from Weather_API import get_weather          # Your weather fetch function
from Database import save_weather            # Your PostgreSQL save function

# Function to handle user messages (must be async in v20+)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract city from message
    city = update.message.text
    print("Received message:", city)  # Debug: See if handler is triggered

    # Get weather data
    temperature, condition = get_weather(city)

    if temperature is not None and condition is not None:
        # Reply to user
        await update.message.reply_text(
            f"Weather in {city}:\n {temperature}°C\n {condition}"
        )

        # Save to PostgreSQL
        save_weather(city, temperature, condition)
    else:
        await update.message.reply_text("City not found or API error.")

# Function to start the bot
def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register the message handler (plain text messages only)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

# Entry point
if __name__ == '__main__':

    start_bot()