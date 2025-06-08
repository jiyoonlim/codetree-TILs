inp=input()
arr=inp.split()
a=int(arr[0]);b=int(arr[1]);c=int(arr[2])

if a<=b and a<=c :
    print(a)
elif b<=c :
    print(b)
else:
    print(c)