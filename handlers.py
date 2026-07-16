from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from bot_config import ADMIN_ID
from admin import upload_template, upload_font
from template_manager import get_templates


MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["📄 إنشاء PDF"],
        ["📁 النماذج", "⚙️ لوحة الأدمن"],
        ["ℹ️ المساعدة"],
    ],
    resize_keyboard=True,
)


ADMIN_MENU = ReplyKeyboardMarkup(
    [
        ["📤 رفع نموذج PDF"],
        ["📂 عرض النماذج", "🗑 حذف نموذج"],
        ["🔤 رفع خط", "📚 عرض الخطوط"],
        ["📍 إضافة حقل", "📋 عرض الحقول"],
        ["🧪 تجربة PDF"],
        ["⬅️ رجوع"],
    ],
    resize_keyboard=True,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 مرحبًا بك في بوت تعديل ملفات PDF",
        reply_markup=MAIN_MENU,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id


    if text == "⚙️ لوحة الأدمن":

        if user_id != ADMIN_ID:
            await update.message.reply_text(
                "❌ ليس لديك صلاحية الوصول."
            )
            return

        await update.message.reply_text(
            "⚙️ لوحة الأدمن",
            reply_markup=ADMIN_MENU,
        )


    elif text == "📤 رفع نموذج PDF":

        if user_id != ADMIN_ID:
            return

        await upload_template(update, context)


    elif text == "🔤 رفع خط":

        if user_id != ADMIN_ID:
            return

        await upload_font(update, context)


    elif text == "📂 عرض النماذج":

        if user_id != ADMIN_ID:
            return

        templates = get_templates()

        if not templates:
            await update.message.reply_text(
                "📭 لا توجد نماذج محفوظة."
            )
            return


        message = "📂 النماذج:\n\n"

        for item in templates:

            try:
                message += (
                    f"🆔 {item['id']}\n"
                    f"📄 {item['name']}\n\n"
                )

            except:

                message += (
                    f"🆔 {item[0]}\n"
                    f"📄 {item[1]}\n\n"
                )


        await update.message.reply_text(message)



    elif text == "🗑 حذف نموذج":

        if user_id != ADMIN_ID:
            return

        await update.message.reply_text(
            "🗑 أرسل رقم ID النموذج الذي تريد حذفه."
        )


    elif text == "📚 عرض الخطوط":

        if user_id != ADMIN_ID:
            return

        await update.message.reply_text(
            "📚 عرض الخطوط سيتم ربطه الآن."
        )


    elif text == "📍 إضافة حقل":

        if user_id != ADMIN_ID:
            return

        await update.message.reply_text(
            "📍 إضافة الحقول سيتم ربطها مع محرر PDF."
        )


    elif text == "📋 عرض الحقول":

        if user_id != ADMIN_ID:
            return

        await update.message.reply_text(
            "📋 عرض الحقول سيتم تفعيله."
        )


    elif text == "🧪 تجربة PDF":

        if user_id != ADMIN_ID:
            return

        await update.message.reply_text(
            "🧪 تجربة إنشاء PDF قيد التطوير."
        )


    elif text == "📄 إنشاء PDF":

        await update.message.reply_text(
            "🚧 سيتم تفعيل إنشاء PDF بعد ربط محرك التعبئة."
        )


    elif text == "📁 النماذج":

        await update.message.reply_text(
            "📁 قسم النماذج."
        )


    elif text == "ℹ️ المساعدة":

        await update.message.reply_text(
            "📌 استخدم الأزرار للتعامل مع البوت."
        )


    elif text == "⬅️ رجوع":

        await update.message.reply_text(
            "🏠 القائمة الرئيسية",
            reply_markup=MAIN_MENU,
        )