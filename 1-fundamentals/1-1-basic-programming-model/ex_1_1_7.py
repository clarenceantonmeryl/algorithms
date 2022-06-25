# a
t: float = 9.0
while abs(t - 9.0/t) > 0.001:
    t = (9.0/t + t) / 2.0
print(t)

# b
sum: int = 0
for i in range(1, 1000):
    for j in range(0, 1):
        sum += 1
print(sum)

# c
i = 1
while i < 1000:
    for j in range(0, i):
        sum += 1
    i *= 2

print(sum)
