import pymysql.cursors
#veritabanı bağlantı cümlesi
connection=pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           db="personeller",
                           charset="utf8mb4",
                           cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        #tek satır okuma
        sql="SELECT`id`, `firstname`,`lastname` FROM `users`"
        cursor.execute(sql)
        for row in cursor.fetchall():
            #tüm satırları okuma
            firstname=str(row["firstname"])
            lastname=str(row["lastname"])
            #ekrana yazdırma
            print("isim:"+firstname)
            print("soyisim:"+lastname)
finally:
    connection.close()