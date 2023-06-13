for i in range(int(input())):
    arr=list(map(int,input().split()))
    min=arr[0]
    for j in range(1,len(arr)):
        if min>arr[j]:
            min=arr[j]
    print(min)
            
