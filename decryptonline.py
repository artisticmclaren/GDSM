import requests,ospatch,zlib,base64

headers = {
    "User-Agent": ""
}

def Decryptl(data):
    return zlib.decompress(base64.b64decode(data.replace('-','+').replace('_','/').encode())[10:],-zlib.MAX_WBITS)

def decrypt_online(id:int):
    ospatch.clear()
    data={
        "levelID": id,
        "secret": "Wmfd2893gb7"
    }    

    req=requests.post(url="http://www.boomlings.com/database/downloadGJLevel22.php",data=data,headers=headers)
    if (req.text=="-1"):
        print("Level does not exist or is private.")
    ldata = req.text.split(":")
    ldata=[":".join(ldata[i:i+2]) for i in range(0, len(ldata), 2)]
    ld=""
    name=""
    for d in ldata:
        d=d.split(":")
        if d[0]=='1':
            print(f'id: {d[1]}')
        if d[0]=='2':
            print(f'name: {d[1]}')
            name=d[1]
        if d[0]=='4':
            ld=d[1]
        if d[0]=='10':
            print(f'downloads: {d[1]}')
        if d[0]=='14':
            print(f'likes: {d[1]}')
        if d[0]=='6':
            print(f'author(pid): {d[1]}')
        if d[0]=='27':
            print(f'hash: {d[1]}')
    print("Found level data...")
    print("Decrypting...")
    f = open(f"levels/{name}","wb")
    f.write(Decryptl(ld))
    print("Decrypted.")

if __name__=="__main__":
    ospatch.clear()
    decrypt_online(int(input("id: ")))
