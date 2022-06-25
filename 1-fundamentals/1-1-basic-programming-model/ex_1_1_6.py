f: int = 0
g: int = 1

for i in range(0, 16):
    print(f, g)
    f = f + g
    g = f - g