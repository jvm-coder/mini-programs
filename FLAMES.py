def rem_match_char(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                a=a[:i]+'*'+a[i+1:]
                b=b[:j]+'*'+b[j+1:]
    return (len(a)+len(b))-(a.count('*')+b.count('*'))

a=input("Enter FIRST name : ")
b=input("Enter SECOND name : ")
a=a.upper()
b=b.upper()
t=rem_match_char(a,b)
res=['FRIENDSHIP','LOVE','AFFECTION','MARRIAGE','ENEMY','SISTER']
while len(res)>1:
    cut=t%len(res)
    if (cut-1)==0:
        res=res[cut:]
    elif (cut-1)==(len(res)-1):
        res=res[:cut]
    elif cut==0:
        res=res[:len(res)-1]
    else:
        res=res[cut:]+res[:cut-1]

print("RELATIONSHIP : ",res[0])


