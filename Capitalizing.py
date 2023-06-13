s=list(map(str,input().split()))
l=len(s)
if l==1:
    print(s[0].capitalize())
elif l==2:
    print(s[0][0].upper()+'.'+s[1].capitalize())
else:
    print(s[0][0].upper()+'.'+s[1][0].upper()+'.'+s[2].capitalize())
    

