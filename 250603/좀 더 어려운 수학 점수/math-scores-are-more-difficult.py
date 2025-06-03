amath, aeng = map(int, input().split())
bmath, beng = map(int, input().split())

if amath == bmath:
    if aeng > beng:
        print("A")
    else:
        print("B")
else:
    if amath > bmath:
        print("A")
    else:
        print("B")