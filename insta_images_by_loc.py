import requests
import json
from geoloc import coordinates

client_id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                              #client ID
client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"                          #client Secret
redirect_uri="http://localhost"                                           #redirect uri. I've set mine to localhost. This can be changed
grant_type="authorization_code"                                           #default option provided by Instagram

req_params={"client_id":client_id, "client_secret":client_secret, \
"redirect_uri":redirect_uri, "grant_type":grant_type, "code":code}

def get_access_token(req_params):
    auth_url="https://api.instagram.com/oauth/authorize/?client_id=" + client_id + "&redirect_uri=" + redirect_uri + "&response_type=code"
    print auth_url
    print "Take this url and paste in your browser. Authorize the app: "+auth_url    #authorization step. need a better way to do this

    redirected_url=raw_input("Now enter the url returned after authorization.\n")    #browser will redirect to a new page whose url will have the code as a response
    code=redirected_url.split('code=')[1]

    request_url="https://api.instagram.com/oauth/access_token"
    r=requests.post(request_url, data=req_params)                      #making a POST request with the client details as parameters

    data=json.loads(r.text)
    access_token=str(data["access_token"])
    return access_token

def media_search(lat,lng,access_token):
    url="https://api.instagram.com/v1/media/search?lat="+lat+"&lng="+lng+"&distance=5000"+"&access_token="+access_token
    print url
    r=requests.get(url)
    resp=json.loads(r.text)
    for i in range(10):                                                         #just getting 10 images. can be changed
        pic_url=resp['data'][i]['images']['standard_resolution']['url']         #getting the image url
        p=requests.get(pic_url)
        f_name=str(location)+ ' pic '+str(i)+'.jpg'
        with open(f_name,'wb') as f:
            f.write(p.content)
            f.close()
        print "got one"

location=raw_input("Enter location.\n")
c=coordinates(location)
lat=str(c[0])
lng=str(c[1])

media_search(lat,lng, get_access_token(req_params))
