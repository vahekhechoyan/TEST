def func(s:str)->int:
    res={}
    for char in s:
        if res.get(char):
            res[char]+=1
        else:
            res[char]=1
    return res

print(func("hello"))                


# with optimization

def func(s:str)->int:
    res={}
    for char in s:
        res[char]=res.get(char,0) +1
    return res

print(func("hello"))


