from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot_config import BOT_TOKEN

from handlers import (
    start,
    menu,
)

from admin import (
    receive_pdf,
    receive_font,
)

app = Application.builder().token(
    BOT_TOKEN
).build()

# أوامر
app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

# ملفات PDF
app.add_handler(
    MessageHandler(
        filters.Document.PDF,
        receive_pdf
    )
)

# جميع الملفات الأخرى
app.add_handler(
    MessageHandler(
        filters.Document.ALL,
        receive_font
    )
)

# الرسائل النصية
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        menu
    )
)

print("🚀 PDF Bot Started")

app.run_polling()