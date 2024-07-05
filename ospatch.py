import os,platform
def clear(a="a"):
    if (platform.system()=="Windows"):
        os.system("cls")
    else:
        os.system("clear")