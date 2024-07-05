import base64,zlib,os,time,shutil
os.system("clear")

def getValue(lsobj:str,id:int): return lsobj[lsobj.index(f"kA{id}")+1]
def itob(i:int): 
    if i==0: return "true" 
    else: return "false"

def levelStats():
    done=False
    os.system("clear")
    name = input("level name >")
    f = open(f"levels/{name}","r")

    data = f.read().split(";")
    objects = []
    for d in data:
        if d==data[len(data)-1]:
            continue
        objects.append(d)
    levelStartObject = objects[0].split(",")
    os.system("clear")
    version="22"
    try: getValue(levelStartObject,22)
    except: version="21"
    if version=="22":
        print(f"""
    {name}:

    Object count: {len(data)-2}
    Is Dual: {itob(getValue(levelStartObject,8))}
    2 Player Mode: {itob(getValue(levelStartObject,9))}
    Mini: {itob(getValue(levelStartObject,3))}
    Platformer: {itob(getValue(levelStartObject,22))}
    Song Offset: {getValue(levelStartObject,13)}
    Song Fade In: {itob(getValue(levelStartObject,15))}
    Song Fade Out: {itob(getValue(levelStartObject,16))}
    Font ID: {getValue(levelStartObject,18)}

    """)
    else:
        print(f"""
    {name}:

    Object count: {len(data)-2}
    Is Dual: {itob(getValue(levelStartObject,8))}
    2 Player Mode: {itob(getValue(levelStartObject,9))}
    Mini: {itob(getValue(levelStartObject,3))}
    Song Offset: {getValue(levelStartObject,13)}
    Song Fade In: {itob(getValue(levelStartObject,15))}
    Song Fade Out: {itob(getValue(levelStartObject,16))}
    Font ID: {getValue(levelStartObject,18)}
    """)
    
    while done==False:
        try: a = input("get info from object >")
        except KeyboardInterrupt: quit()
        if (a=="exit"):
            done==True
            quit()
        aid = int(a)
        objData = data[aid].split(",")
        id = objData[objData.index('1')+1]
        x = objData[objData.index('2')+1]
        y = objData[objData.index('3')+1]
        print(f"Object {aid}:\n\nID:{id}\nX:{x}\nY:{y}") 
if __name__=="__main__":
    print("""
    lvlstat v1.0.0
        
    """)
    levelStats()