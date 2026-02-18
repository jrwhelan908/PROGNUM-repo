fib = [1, 2]

for i in range (98):
    fib.append(fib[-1] + fib[-2])

print("The 100th term :", fib[99])
