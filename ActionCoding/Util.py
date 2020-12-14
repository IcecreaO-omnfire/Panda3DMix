from collections import *
def countDict(processing):
    try:
        b=Counter(processing)
        c={v:k for (k,v) in b.items()}
        c[2]
    except Exception as ex:
        print(ex)
    