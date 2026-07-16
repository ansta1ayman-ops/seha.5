# database.py

import sqlite3


DB_NAME = "database.db"


def get_connection():

    conn = sqlite3.connect(
        DB_NAME
    )

    conn.row_factory = sqlite3.Row

    return conn



def create_tables():

    conn = get_connection()
    cursor = conn.cursor()


    # =====================
    # جدول نماذج PDF
    # =====================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS templates (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            file_path TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )


    # =====================
    # جدول الحقول
    # =====================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS fields (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            template_id INTEGER NOT NULL,

            field_name TEXT NOT NULL,

            page INTEGER DEFAULT 0,

            x REAL NOT NULL,

            y REAL NOT NULL,

            font_size INTEGER DEFAULT 12,

            font_name TEXT DEFAULT 'arial.ttf',

            FOREIGN KEY(template_id)
            REFERENCES templates(id)

        )
        """
    )


    # =====================
    # جدول الخطوط
    # =====================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS fonts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            font_name TEXT NOT NULL,

            file_path TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )


    conn.commit()
    conn.close()



# =====================
# تنفيذ أوامر
# =====================

def execute(
    query,
    params=()
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        query,
        params
    )

    conn.commit()

    conn.close()



# =====================
# جلب عنصر واحد
# =====================

def fetchone(
    query,
    params=()
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        query,
        params
    )

    result = cursor.fetchone()

    conn.close()

    return result



# =====================
# جلب عدة عناصر
# =====================

def fetchall(
    query,
    params=()
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        query,
        params
    )

    result = cursor.fetchall()

    conn.close()

    return result



# إنشاء الجداول عند تشغيل الملف
create_tables()