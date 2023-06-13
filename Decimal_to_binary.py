for i in range(int(input())):
    """ Dec_number= int(input())
    binary=""
    while Dec_number!=0:
        rem=Dec_number%2
        binary+=str(rem)
        Dec_number//=2
    print(binary[::-1])"""
    
    deci_number=int(input())    
    binary=0
    i=0
    while deci_number!=0:
        rem=(deci_number%2)*(10**i)
        binary+=rem
        deci_number//=2
        i+=1
        print(binary)
        
        
