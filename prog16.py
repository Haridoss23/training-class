h,d=map(int,input().split())
for i in range (h+1,d):
    for j in range(2,i):
      if (i%j==0):
        break
    else:
        print(j,end=' ')
