def to_binary_string(n: int):
    s: str = ""
    k = n
    while k > 0:
        s = str(k % 2) + s
        k = int(k/2)

    return s


print(to_binary_string(10))
