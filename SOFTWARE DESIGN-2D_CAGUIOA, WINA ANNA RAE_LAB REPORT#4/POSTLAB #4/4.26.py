def tower(a,s1,s2,s3):
    
    if a == 1:
        print("Move first disc to s1", s1 ,"to s2", s2)
        return
    tower(a-1,s1,s2,s3)
    print ("Move disc ", a ,"from ",s1,"to",s2 )
    tower(a-1,s1,s2,s3)
   

a= 3
print(tower(a,'a','b','c'))
