def fibonacci(n):
    print('calculating  elif', n)
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:

        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        #print('calculating 2nd elif n', n)
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    print('calculating 2nd elif ', n)

print(fibonacci(6))