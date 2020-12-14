def findPair(b):
    u=[]
    k=[]
    
    for a in b:
        try:
            if a in k:
                u.append(a)
                raise ValueError(a)
            #print(u)
            k.append(a)
            #k.append(a)
            
        except Exception as ex:
            print(ex)
    return u