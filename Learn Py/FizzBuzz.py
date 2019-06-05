for x in range(100):
    print(x)
    if x%3==0 and x%5==0:
        print("FizzBuzz")

    if x%5 == 0:
        print("Fizz")
    if x%3==0:
        print("Buzz")
