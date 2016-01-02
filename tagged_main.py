import os
import requests
import sqlite3

name=raw_input('name?\n')
db_name=name+'.sqlite'

conn=sqlite3.connect(db_name)                        #database file
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Urls_Done (num NUMBER, url TEXT)''')

cur.execute('''
SELECT COUNT(url) FROM Urls_Done''')

count=cur.fetchone()[0]+1

cur.execute('''
SELECT url FROM Urls_To_Do WHERE (num>=? and num<?)''',(count,count+30))

urls=[el[0] for el in cur.fetchall()]

directory='D:/PY/Instagram/'+name+'/'
if not os.path.exists(directory):
    os.makedirs(directory)

for url in urls:
    r=requests.get(url)
    f_name=os.path.join(directory, name+'_'+str(count)+'.jpg')
    with open(f_name,'wb') as f:
        f.write(r.content)
        f.close()
    print url
    cur.execute('''
    INSERT INTO Urls_Done (num,url) VALUES (?,?)''',(count,url))
    conn.commit()
    count+=1
