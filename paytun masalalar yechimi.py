 k,n=map(int,input('sonlarni kiriting: ').split())
 for i in range(0,n):
     print(k,end=" ")

 for i in range(1,11):
     for x in range(1,11):
         print(str(x)+"*"+str(i)+"="+str(i*x),end="   ")
     print()

 print("salom"+" Ali"+str(45))


# archani yasash kodi    
 n=int(input('n= '))
 for i in range(n):
     print(((n-i)*"*"+(2*i+1)*" ")+(n-i)*"*")
 for j in range(n):
     print(((n-1)*"*"+(3*" "))+(n-1)*"*")
     if j==2:
         break
    
#        *
#      * * * 
#    * * * * * 
#  * * * * * * *
#      * * * 
#      * * *
#      * * *
    
    
# 5
# 1
# 12
# 123
# 1234
# 12345

 n = int(input("son: "))
 for i in range(1,n+1):
     for x in range(1,i+1):
         print(x,end="")
     print()


# 1
# 23
# 456
# 78910
# 1112131415

 n = int(input("son: "))
 s=1
 for i in range(1,n+1):
     for x in range(1,i+1):
         print(s,end="")
         s+=1
     print()


# while operatori ichiga shart berish mumkiun 
 a=1
 while a<=100:
    print(a)
    a+=1


 a=1
 while a<=100:
    print(a)
    a+=1
    if a==96:
         break

 a=0
 while a<=100:
     a+=1
     if a==96:
         continue
     print(a)

 a=0
 while a<=100:
     a+=1
     if a%2==1:
         continue
     print(a)