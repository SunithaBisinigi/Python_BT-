for i in range(int(input())):
    Array = list (map (int,input().split()))
    number= int(input())
    for j in Array:
        if number==j:
            ans="Yes"
            break
        else:
            ans="NO"
    print(ans)
