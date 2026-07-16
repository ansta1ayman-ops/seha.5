import os

from telegram import Update
from telegram.ext import ContextTypes

from database import add_template, fetchone
from fonts import save_font

WAITING_FOR_PDF = set()
WAITING_FOR_FONT = set()

TEMPLATES_DIR = "templates"

os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs("fonts", exist_ok=True)


# =========================
# رفع نموذج PDF
# =========================

async def upload_template(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    WAITING_FOR_PDF.add(update.effective_user.id)

    await update.message.reply_text(
        "📤 أرسل ملف PDF."
    )


async def receive_pdf(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    if user_id not in WAITING_FOR_PDF:
        return

    document = update.message.document

    if document is None:
        return

    if not document.file_name.lower().endswith(".pdf"):

        await update.message.reply_text(
            "❌ يجب إرسال ملف PDF فقط."
        )
        return

    existing = fetchone(
        "SELECT * FROM templates WHERE name=?",
        (document.file_name,)
    )

    if existing:

        WAITING_FOR_PDF.discard(user_id)

        await update.message.reply_text(
            "⚠️ النموذج موجود مسبقاً."
        )
        return

    telegram_file = await context.bot.get_file(
        document.file_id
    )

    save_path = os.path.join(
        TEMPLATES_DIR,
        document.file_name
    )

    await telegram_file.download_to_drive(
        save_path
    )

    add_template(
        document.file_name,
        save_path
    )

    WAITING_FOR_PDF.discard(user_id)

    await update.message.reply_text(
        "✅ تم حفظ النموذج بنجاح."
    )


# =========================
# رفع الخطوط
# =========================

async def upload_font(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    WAITING_FOR_FONT.add(
        update.effective_user.id
    )

    await update.message.reply_text(
        "🔤 أرسل ملف خط TTF أو OTF."
    )


async def receive_font(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    if user_id not in WAITING_FOR_FONT:
        return

    document = update.message.document

    if document is None:
        return

    file_name = document.file_name.lower()

    if not (
        file_name.endswith(".ttf")
        or
        file_name.endswith(".otf")
    ):

        await update.message.reply_text(
            "❌ أرسل ملف خط فقط."
        )
        return

    telegram_file = await context.bot.get_file(
        document.file_id
    )

    file_bytes = await telegram_file.download_as_bytearray()

    save_font(
        document.file_name,
        file_bytes
    )

    WAITING_FOR_FONT.discard(
        user_id
    )

    await update.message.reply_text(
        f"✅ تم حفظ الخط:\n{document.file_name}"
    )