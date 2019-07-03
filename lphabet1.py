print("Enter");
b = input("character: ");
if b == '0':
    exit();
else:
    if((b>='a' and b<='z') or (b>='A' and b<='Z')):
    	print(b, "is an alphabet.");
    else:
    	print(b, "is not an alphabet.");
