for i in range(int(input())):
    arr=list(map(int,input().split()))
    check=arr[0]
    for j in range(len(arr)):
        for k in range(j+1,len(arr)):
            if arr[j]>arr[k]:
                arr[j],arr[k]= arr[k],arr[j]
    print(arr)
        
