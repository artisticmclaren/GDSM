import base64,zlib,os,time,ospatch

ospatch.clear("clear")

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

def create_gmd():
    level = input("level file (no spaces): ")
    name = input("level name: ")
    creator = input("creator: ")
    f = open(f"levels/{level}","rb")
    data=f.read()       
    xml = f'<?xml version="1.0"?><plist version="1.0" gjver="2.0"><dict><k>kCEK</k><i>4</i><k>k2</k><s>{name}</s><k>k4</k><s>{data}</s><k>k5</k><s>{creator}</s><k>k101</k><s>0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0</s><k>k13</k><t /><k>k21</k><i>2</i><k>k16</k><i>1</i><k>k80</k><i>84</i><k>k83</k><i>611</i><k>k50</k><i>42</i><k>k47</k><t /><k>k48</k><i>4</i><k>kI1</k><r>172.789</r><k>kI2</k><r>14.3704</r><k>kI3</k><r>1.2</r><k>kI6</k><d><k>0</k><s>0</s><k>1</k><s>0</s><k>2</k><s>0</s><k>3</k><s>0</s><k>4</k><s>0</s><k>5</k><s>0</s><k>6</k><s>0</s><k>7</k><s>0</s><k>8</k><s>0</s><k>9</k><s>0</s><k>10</k><s>0</s><k>11</k><s>0</s><k>12</k><s>0</s><k>13</k><s>0</s></d></dict></plist>'
    f = open(f"{name}.gmd","w")
    f.write(xml)
    print(f"Created {name}.gmd in working directory.")

if __name__=="__main__":
    print("gmdcreate v1.0.0\n")
    create_gmd()