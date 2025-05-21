h,w = map(int, input().split())
b = int(((10000) * w ) / (h * h))
print(f"{b}")
if b >= 25:
    print("Obesity")