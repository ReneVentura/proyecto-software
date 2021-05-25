import hashlib as hash

def pw_gen(plain):
    r = hash.md5(plain.encode())
    num = int(r.hexdigest(), 16)
    width = len(str(num))
    return((plain + '_' + str(num))[0:50])
    #return plain
    
    
#print(pw_gen('r'))