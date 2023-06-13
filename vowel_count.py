n=input()
c=0
vowel=['a','e','i','o','u']
for i in n:
    if i not in vowel:
        c+=1
    else:
        break
if c>=4:
    print('no')
else:
    print('yes')
        
