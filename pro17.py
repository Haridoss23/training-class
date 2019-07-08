num=int(input())
hd=num
sum=0
while num>0:
  b=num%10
  sum=sum+b*b*b
  num=num//10
if hd==sum:
  print("yes")
else:
  print("no")
