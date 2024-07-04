import os

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

os.system("clear")

def itob(i:int): 
    if i==0: return "true" 
    else: return "false"

def colorstat():
    file = input("decrypted level file >")
    try:
        open(file)
    except:
        print("File not found.")
        colorstat()
    f = open(file,"r")
    data = f.read().split(",")
    try:
        data.index("kS38")+1
    except:
        print("Pre 2.0 levels are not supported!")
        colorstat()
    colorstring = data[data.index("kS38")+1].split("|")
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
        rgb = f"{values[values.index("1")+1]}, {values[values.index("2")+1]}, {values[values.index("3")+1]}"
        torgb = f"{values[values.index("11")+1]}, {values[values.index("12")+1]},{values[values.index("13")+1]}"
        print(f"\nFrom RGB: {rgb}\nTo RGB: {torgb}\nOpacity: {values[values.index("7")+1]}\nIs Blending: {isBlending}\n")

if __name__=="__main__":
    print("colorstat v1.0.1\n")
    colorstat()
