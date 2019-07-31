doss=int(input("enter the number:"))
don=0
temp=doss
while temp>0:
  digit=temp%10
  don+=digit**3
  temp//=10
if doss==don:
 print(doss,"yes")
else:
 print(doss,"no")
