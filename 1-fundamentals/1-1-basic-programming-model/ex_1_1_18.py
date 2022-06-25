def mystery(a: int, b: int):
    if b == 0:
        return 0
    if b % 2 == 0:
        return mystery(a + a, int(b / 2))
    return mystery(a + a, int(b / 2)) + a


print(mystery(2, 25))
print(mystery(3, 11))
