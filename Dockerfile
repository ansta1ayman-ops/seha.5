FROM python:3.11-slim

WORKDIR /app

# تثبيت متطلبات النظام الخاصة بـ PDF والخطوط
RUN apt-get update && apt-get install -y \
    fonts-dejavu \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملف المكتبات
COPY requirements.txt .

# تثبيت مكتبات البوت
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات المشروع
COPY . .

# تشغيل البوت
CMD ["python", "main.py"]