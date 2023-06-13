for i in range(int(input())):
    """Binary_number=input()[::-1]
    result=0
    for j in range(len(Binary_number)):
        result+=(int(Binary_number[j])*(2**j))
    print(result)"""
    
    binary_number=int(input())
    dec=0
    i=0
    while binary_number!=0:
        rem=binary_number%10
        dec+=(rem*(2**i))
        binary_number//=10
        i+=1
        print(dec)
        
    
