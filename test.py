

le=10
li=[1,2,3,4,5,6,7,8,0,0]

i=le-1
while i>=0:
    j=0
    
    
    if li[i]!=0:
        while i>=j:
            
            t=li[i]
            li[i]=li[j]
            li[j]=t
            i=i-1
            j=j+1
        
        break
    else:
        i=i-1
        continue

print li