import sqlite3
con = sqlite3.connect('C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
cursor = con.cursor()
cursor.execute("SELECT url FROM urls")
urls = cursor.fetchall()
for url in urls:
    print(str(url[0]) + '')
