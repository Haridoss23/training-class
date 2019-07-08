h=int(input())
if h > 1:
    for d in range(2,h):
        if(h%d==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
