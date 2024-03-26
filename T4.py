x=lambda n:1 if n<=1 else x(n-1)+x(n-2)
print(x(27))


#  with recursive
def x(n:int)->int:
    if n<=1:
        return 1
    else:
        return x(n-1)+x(n-2)
    

print(x(27))


# without recursive

def x(n:int)->int:
    if n<=1:
        return 1
    else:
        f=[1,1]
        for i in range(2,n+1):
            f.append(f[-1]+f[-2])

    return f[n]

print(x(27))



