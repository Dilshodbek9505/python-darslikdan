#1
# a=int(input())
# p=4*a
# print(p)
#2
# a=int(input())
# s=a*a
# print(s)
#3
# a,b=map(int,input().split())
# s=a*b
# p=2*(a+b)
# print(s)
# print(p)
#4
# d=int(input())
# l=3,14*d
# print(l)
#5
# a=int(input())
# v=a**3
# s=6*a**2
# print(v)
# print(s)
#6
# a,b,c=map(int,input().split())
# v=a*b*c
# s=2*(a*b+b*c+a*c)
# print(v,s)
#7
# r=int(input())
# p=3.14
# l=2*p*r
# s=p*r**2
# print(l,s)
#8
# a,b=map(int,input().split())
# x=(a+b)/2
# print(x)
#9
# a,b=map(int,input().split())
# y=(a*b)**0.5
# print(y)
#10
# x,y=map(int,input().split())
# a=(x+y)
# b=(x*y)
# c=x**2
# d=y**2
# print(a,b,c,d)
#11
# x,y=map(int,input().split())
# a=x+y
# b=x*y
# c=abs(x)
# d=abs(y)
# print(a,b,c,d)
#12
# a,b=map(int,input().split())
# c=(a**2+b**2)**0.5
# print(c)
# p=a+b+c
# print(p)
#13
# r1,r2=map(int,input().split())
# if(r1<r2):
#     r1,r2=r2,r1
#     S1=3.14*r1
#     S2=3.14*r2
# print(S1,S2)
# S3=S1-S2
# print(S3)
#14
# r=int(input())
# l=2*3.14*r
# print(l)
# s=3.14*r**2
# print(s)
#15
# d=int(input())
# r=d/2
# l=2*3.14*r
# s=3.14*r**2
# print(l,s)
#16
# x1,x2=map(int,input().split())
# a=abs(x1-x2)
# print(a)
#17
# a,b,c=map(int,input().split())
# x=abs(a-b)
# y=abs(b-c)
# z=x+y
# print(x,y,z,sep=('\n'))
#18
# import random
# a,b=map(int,input().split())
# c=random.randint(a+1,b-1)
# x=abs(a-c)
# y=abs(b-c)
# z=x*y
# print(c,x,y,z,sep=('\n'))
#19
# x1,x2,y1,y2=map(int,input().split())
# a=abs(x1-x2)
# b=abs(y1-y2)
# s=a*b
# p=2*(a+b)
# print(a,b,s,p,sep=('\n'))
#20
# x1,x2,y1,y2=map(int,input('kordinatalarni kiriting ').split())
# a=((x2-x1)**2+(y2-y1)**2)**0.5
# print(a)
#29
# x,y=map(int,input().split())
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if(x2>x and x>x1 and y1>y and y>y2):
#     print('togri')
# else:
#     print('notogri')
#30
# a,b,c=map(int,input().split())
# if(a==b and b==c and a==c):
#     print('teng tomonli')
# else:
#     print('teng tomonlimas')
#31
# a,b,c=map(int,input().split())
# if(a==b and a<c and b<c):
#     print('teng yonli')
# elif(a==b==c):
#     print('teng tomonli')
# else:
#     print('uchburchak emas')
#32
# a,b,c=map(int,input().split())
# if(a**2+b**2==c**2):
#     print('rost')
# else:
#     print('yolgon')
#33
# a,b,c=map(int,input().split())
# if((a+b)>c):
#     print('uchburchak mavjud')
# else:
#     print('uchburchak mavjud emas')
#34
# x,y=map(int,input().split())
# if((x+y)%2!=0):
#     print('oq katak')
# else:
#     print('qora katak')
#35
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# a=((x1+y1)%2==0) and ((x2+y2)%2==0)
# b=((x1+y1)%2!=0) and ((x2+y2)%2!=0)
# if(a or b):
#     print("bir xil rang ")
# else:
#     print('bir xil rang emas')
#36
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if(x1==x2 or y1==y2):
#     print('ota oladi')
# else:
#     print('ota olmaydi')
#37
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if(x1==x2 and y1<y2 and abs(y1-y2)==1):
#     print('shox tepaga yuradi')
# elif(x1==x2 and y1>y2 and abs(y1-y2)==1):
#     print('shox patga yuradi')
# elif(y1==y2 and x1<x2 and abs(x1-x2)==1):
#     print('shox ongga yuradi')
# elif(y1==y2 and )
#38
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if((x1+x2)==(y1+y2)):
#     print('fil yuradi')
# else:
#     print('fil yurmaydi')
#39   
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# if(x1<x2 and y1==y2):
#     print('ongga yuradi')
# elif(x1>x2 and y1==y2):
#     print('chapga yuradi')
# elif(x1==x2 and y1<y2):
#     print('tepaga yuradi')
# elif(x1<x2 and y1<y2):
#     print('ong yuqoriga uradi')
# elif(x1>x2 and y1<y2):
#     print('chap yuqoriga yuradi')
# else:
#     print('farzin yurmaydi')



# 3 dars
#1
# k,n=map(int,input('sonlarni kiriting: ').split())
# for i in range(0,n):
#     print(k,end=" ")
#2
# a,b=map(int,input('sonlarni kiriting: ').split())
# s=int()
# for i in range(a,b+1)[::1]:
#     s=s+1
#     print(i,end=" ")
# print(sep=('\n'))
# print(s)
#3
# a,b=map(int,input('sonlarni kiriting: ').split())
# s=int()
# for i in range(a,b+1)[::-1]:
#     s+=1
#     print(i,end=" ")
# print(sep=('\n'))
# print(s)
#4
# b=int(input('kanfet narxini kiriting= '))
# for a in range(1,11):
#     print(a,' kg=',a*b)
#5
# b=int(input('kanfet narxini kiriting= '))
# for a in range(10):
#     print(a/10,'kg=',(a/10)*b)
#6
# b=int(input('kanfet narxini kiriting= '))
# for a in range(12,20):
#     print(a/10,' kg=',(a/10)*b)
#7
# a,b=map(int,input('sonlarni kiriting= (a<b): ').split())
# d=0
# for c in range(a,b):
#     d+=c
#     print(d)
#8
# a,b=map(int,input('sonlarni kiriting= ').split())
# d=1
# for c in range(a,b):
#     d*=c
#     print(d)
#9
# d=0
# a,b=map(int,input('sonlarni kiriting= (a<b): ').split())
# for c in range(a,b):
#     d+=c**2
# print(d)
#10
# s=0
# n=int(input('sonni kiriting(n>0)= '))
# for i in range(1,n+1):
#     s+=1/i
#     print(s)
#11
# s=0
# n=int(input('sonni kiriting(n>0)= '))
# for i in range(n,2*n+1):
#     s+=i**2
# print(s)
#12
# s=1
# n=int(input('sonni kiriting(n>0)= '))
# for i in range(11,n+11):
#     s*=i/10
# print(s)
#13
# s=0
# n=int(input('sonni kiriting(n>0)= '))
# for i in range(11,n+11):
#     s+=(-1)**(i+1)*i/10
# print(s)
#14
# s=0
# n=int(input('sonni kiriting(n>0)= '))
# for i in range(1,n+1):
#     print(i) 
#     s+=i*2-1
# print(s) 
#15
# s=1
# a,n=map(int,input('sonlarni kiriting= ').split())
# for i in range(1,n+1):
#     s=s*a
# print(s)
#16
# s=1
# a,n=map(int,input('sonlarni kiriting= ').split())
# for i in range(1,n+1):
#     s*=a
#     print(s)
#17
# a,n=map(int,input('sonlarni kiriting= ').split())
# s=1
# t=0
# for i in range(1,n+1):
#     s*=a
#     t+=s
#     print(s)
# print(t+1)
    