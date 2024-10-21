import base64,zlib,os,ospatch,time,levelstats,creategmd,colorstat,decryptonline
ospatch.clear("ospatch.clear")
#         this option is decrypted, do not try to modify this file to load CCGameManager.dat
saves = ['CCGameManager.dat','CCLocalLevels.dat']

decrypted_save=""   

def getLevelName(level,k):
    r = level.split(f"</s><k>k{k}</k>")[0]
    if (len(r)>20):
        return ""
    return r

def Xor(path,key):
    fr = open(path,'rb')
    data = fr.read()
    fr.close()
    
    res = []
    for i in data:
        res.append(i^key)
    return bytearray(res).decode()
 
def Decrypt(data):
    return zlib.decompress(base64.b64decode(data.replace('-','+').replace('_','/').encode())[10:],-zlib.MAX_WBITS)
def Encrypt(data):
    return base64.b64encode(data.replace('+','-').replace('/','_').encode())

def FullDecrypt():
    for level in os.listdir("levels"):
        os.remove(f"levels/{level}")
    ospatch.clear("ospatch.clear")
    try: os.remove("CCLocalLevels.dat.txt")
    except: pass
    print("Decrypting...")
    read = open("path.txt").readline()
    fPath = read.replace("\n","")
    res = Xor(fPath+saves[1],11)
    fin = Decrypt(res)

    fw = open(f'tmp/{saves[1]}.txt','wb')
    fw.write(fin)
    fw.close()

    print("Finished Decrpt.")
    s = open("tmp/CCLocalLevels.dat.txt","r")
    decrypted_save = s.read()
    time.sleep(2)
    ospatch.clear("ospatch.clear")

    levels=[]

    id=1
    levelCount=0
    finished=False

    print("Finding levels...")
    time.sleep(2)
    ospatch.clear("ospatch.clear")
    while not finished:
        clevel=""
        try: clevel = getLevelName(decrypted_save.split("<k>k2</k><s>")[id],4)
        except IndexError: 
            finished=True 
            continue
        
        if (clevel!=""):
            print(f"Found \"{clevel}\"...")
            id+=1
            levelCount+=1
            levels.append(clevel)
        else:
            id+=1
    ospatch.clear("ospatch.clear")
    #os.remove("tmp/CCLocalLevels.dat.txt")
    print(f"Levels: {levelCount}")
    print("""
    What would you like to do with these levels?
    [1] Decrypt specific level
    [2] Decrypt all levels
          
          """)
    a=input(">")
    if (a.lower()=="1"):
        ospatch.clear("ospatch.clear")
        l = input("level number (order in list) >")
        o = int(l)-1
        print(f"Decrypting \"{levels[o]}\"")
        encryptedld="H4sIAAAAAAAA"+decrypted_save.split("<s>H4sIAAAAAAAA")[1+o].split("</s>")[0]
        decryptedld=Decrypt(encryptedld)
        f = open(f"levels/{levels[o]}","wb")
        f.write(decryptedld)
        print(f"Decrypted \"{levels[o]}\"")
        time.sleep()
        exit()
    else:
        ospatch.clear("ospatch.clear")
        pass
    
    
    for i in levels:
        lname = levels[levels.index(i)]
        print(f"Decrypting \"{lname}\"...")
        encryptedld="H4sIAAAAAAAA"+decrypted_save.split("<s>H4sIAAAAAAAA")[1+levels.index(i)].split("</s>")[0]
        decryptedld=Decrypt(encryptedld)
        f = open(f"levels/{lname.replace(" ","")}","wb")
        f.write(decryptedld)
    ospatch.clear("ospatch.clear")
    print("""
    What would you like to do with your decrypted levels?
    [1] Get level stats of specific level
    [2] Create .gmd file
    [3] Quit
    
        """)
    a = input("> ")
    if a=="1":
        ospatch.clear("ospatch.clear")
        print("[1] general level stats\n[2] level color stats")
        a = input(">")
        if a=="1": levelstats.levelStats()
        elif a=="2": colorstat.colorstat()
    elif a=="2":
        creategmd.create_gmd()
    else:
        quit()

def EncryptIntoSave():
    ospatch.clear("ospatch.clear")
    e = open("encrypt.txt","r")
    print(Encrypt(e.read()))
    e.close()

print("""
gdsavemgr  v1.1.0

[1] Decrypt levels into 'levels' directory
[2] Decrypt .gmd file
[3] Decrypt online level

      """)
a = input(">")
if (a.lower()=="1"):
    FullDecrypt()
elif (a.lower()=="2"):
    l = input("file: ")
    fn = l
    ln = fn.replace(".gmd","")
    print(f"Decrypting {ln}...")
    f = open(fn,"r")
    xml=f.read()
    encrypted_data = xml.split("<k>k4</k><s>")[1].split("</s>")[0]
    try: data = Decrypt(xml.split("<k>k4</k><s>")[1].split("</s>")[0])
    except:
        data=encrypted_data
        r = open(f"levels/{fn.replace(".gmd","")}","w")
        r.write(data)
        print(f"Decrypted {ln}")
        quit()
    r = open(f"levels/{fn.replace(".gmd","")}","wb")
    r.write(data)
    print(f"Decrypted {ln}")
elif (a=="3"):
    decryptonline.decrypt_online(int(input("id: ")))