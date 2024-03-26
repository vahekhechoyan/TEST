ls=[[1,2,3],[3,4,5],[5,6,7]]

res=[[i+j for i in range(1,4)]for j in range(0,6,2)]


res=[]
for i in range(1,4):
    tmp=[]
    for j in range(0,6,2):
        tmp.append(i+j)
    res.append(tmp)    

    
