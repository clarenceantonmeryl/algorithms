class Fibonacci:

    def __init__(self):
        for n in range(0, 90):
            print(f"{n} {self.fibonacci(n)}")

    def fibonacci(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


fib = Fibonacci()
