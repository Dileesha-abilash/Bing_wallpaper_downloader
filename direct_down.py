import requests
import sys
#simple chnage
ary = open("downs.txt","r").readlines()


for i in range(len(ary)):
    if i<=(int(sys.argv[1])-1):
        print("downloading ",i)
        r = requests.get(ary[i], allow_redirects=True)
        g= str(i)+".jpg"
        open(g, 'wb').write(r.content)