'''builds a database of recent Instagram photos tagged by the name you give'''

import requests
import json
import sqlite3

tag = raw_input('Name?\n')

client_id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                              #client ID
client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri. I've set mine to localhost. This can be changed
grant_type="authorization_code"                                           #default option provided by Instagram

db_name=tag+'.sqlite'
conn=sqlite3.connect(db_name)
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Urls_To_Do (num NUMBER, url TEXT)''')

cur.execute('''
SELECT COUNT(url) FROM Urls_To_Do''')

count=cur.fetchone()[0]+1

def get_access_token():
    auth_url="https://api.instagram.com/oauth/authorize/?client_id=" + client_id + "&redirect_uri=" + redirect_uri + "&response_type=code"
    print auth_url
    print "Take this url and paste in your browser. Authorize the app:\n"+auth_url    #authorization step. need a better way to do this

    redirected_url=raw_input("Now enter the url returned after authorization.\n")    #browser will redirect to a new page whose url will have the code as a response
    code=redirected_url.split('code=')[1]
    req_params={"client_id":client_id, "client_secret":client_secret, "redirect_uri":redirect_uri, "grant_type":grant_type, "code":code}
    request_url="https://api.instagram.com/oauth/access_token"
    r=requests.post(request_url, data=req_params)                      #making a POST request with the client details as parameters

    data=json.loads(r.text)
    access_token=str(data["access_token"])
    return access_token


def build_db(access_token, tag,count):
    base_url='https://api.instagram.com/v1/tags/' + tag + '/media/recent'
    r=requests.get(base_url, params={'access_token':access_token})              #first request
    for i in range(1,11):                                                       #next_url is provided in each response
        resp=json.loads(r.text)
        for el in resp['data']:
            url=el['images']['standard_resolution']['url']
            cur.execute('''
            INSERT INTO Urls_To_Do (num, url) VALUES (?,?)''', (count,url))
            conn.commit()
            count+=1
        next_url=resp['pagination']['next_url']
        r=requests.get(next_url)

build_db(get_access_token(), tag, count)
