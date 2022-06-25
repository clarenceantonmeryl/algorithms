def check_floats(x: float, y: float):
    if 0 < x < 1 and 0 < y < 1:
        return True
    else:
        return False


print(check_floats(1.0, 1.5))
print(check_floats(0.9, 0.3))
