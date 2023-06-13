for i in range(int(input())):
    num1,num2=map(int,input().split())
    
    """def factors(n):
        facts=[]
        for j in range(1,n+1):
            if n%j==0:
                facts.append(j)
        return (facts) 
    num1_facts=(factors(num1))
    num2_facts=factors(num2)
    ans=[]
    for j in num1_facts:
        if j in num2_facts:
            ans.append(j)
    print(max(ans))"""
    
    for j in range(1,max(num1,num2)):
        if num1%j==0 and  num2%j==0:
            ans=j
    print(ans)
          
    
    
        
   
