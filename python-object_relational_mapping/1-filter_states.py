#!/usr/bin/python3
Tis module connects to a MySQL database and lists all states
with  name starting with N (upper N) from the database hbtn_0e_0_usa.
""
import sys
import MySQLdb

if __name__ == "__main__":
    # 1. قراءة المدخلات
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

    # 3. استعلام الـ JOIN لربط المدن بالولايات
    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # 4. جلب وطباعة النتائج
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # 5. إغلاق الاتصال
    cursor.close()
    db.close()
