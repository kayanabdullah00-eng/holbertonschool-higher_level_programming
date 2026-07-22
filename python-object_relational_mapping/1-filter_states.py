#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # 1. قراءة المدخلات الممررة عبر السطر البرمجي
    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]

    # 2. إنشاء الاتصال بقاعدة البيانات
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_password,
        db=db_name
    )

    # 3. إنشاء الـ Cursor وتحديد الاستعلام الشرطي
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY states.id ASC"
    )

    # 4. جلب جميع الصفوف المطابقة للشرط وطباعتها
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # 5. إغلاق الـ Cursor والاتصال
    cursor.close()
    db.close()
