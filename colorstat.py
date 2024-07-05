import os,ospatch

def prettify_colorid(id): # proper yandere dev code >:)
    if id==1000:
        return f"BG ({id})"
    elif id==1001:
        return f"G1 ({id})"
    elif id==1002:
        return f"LINE ({id})"
    elif id==1003:
        return f"3DL ({id})"
    elif id==1004:
        return f"OBJ ({id})"
    elif id==1005:
        return f"P1 ({id})"
    elif id==1006:
        return f"P2 ({id})"
    elif id==1007:
        return f"LBG ({id})"
    elif id==1009:
        return f"G2 ({id})"
    elif id==1010:
        return f"BLACK ({id})"
    else:
        return id

ospatch.clear("clear")

def itob(i:int): 
    if i==0: return "true" 
    else: return "false"

def colorstat():
    file = input("decrypted level file >")
    try:
        open(f"levels/{file}")
    except:
        print("File not found.")
        colorstat()
    f = open(f"levels/{file}","r")
    data = f.read().split(",")
    try:
        data.index("kS38")+1
    except:
        print("Pre 2.0 levels are not supported!")
        colorstat()
    colorstring = data[data.index("kS38")+1].split("|")
    ospatch.clear()
    print("=== colors ===\n")
    for color in colorstring:
        if (color==""): continue
        values = color.split("_")
        channel = values[values.index("6")+1]
        isBlending="false"
        try:
            isBlending = str(itob(int(values[values.index("5")+1])))
        except:
            isBlending="false"
        print(f"== Data for color channel {prettify_colorid(int(channel))} ==")
        rgb = f"{values[values.index("1")+1]},{values[values.index("2")+1]},{values[values.index("3")+1]}"
        rgbValues = rgb.split(",")
        opacity = values[values.index("7")+1]
        copied=False
        copiedColorID=0
        try: 
            int(values[values.index("9")+1])
            copied=True
        except: pass

        if (copied):
            copiedColorID = int(values[values.index("9")+1])
            try: opacity=values[values.index("17")+1]
            except: pass
            for colorc in colorstring:
                vl = colorc.split("_")
                try: 
                    if int(vl[vl.index('6')+1])==copiedColorID:
                        rgb = f"{vl[vl.index("1")+1]},{vl[vl.index("2")+1]},{vl[vl.index("3")+1]}"
                        rgbValues = rgb.split(",")
                except:
                    pass
                #print(colorstring.index(colorc))
        data=f"\nFrom RGB: {rgb} \033[38;2;{int(rgbValues[0])};{int(rgbValues[1])};{int(rgbValues[2])}m██\033[0m"
        if (copied):
            data+=f"\nCopying: {prettify_colorid(copiedColorID)}"
        data+=f"\nOpacity: {opacity}\nIs Blending: {isBlending}\n"
        print(data)

if __name__=="__main__":
    print("colorstat v1.1.0\n")
    colorstat()
