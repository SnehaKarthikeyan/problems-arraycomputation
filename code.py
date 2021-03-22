Coding:

n=int(input())
a=list(input().split(" "))
count=0
for i in range(0,n-2):
        print(int(a[i])*int(a[i+1]),end=" ")
print(int(a[n-2])*int(a[n-1]))
