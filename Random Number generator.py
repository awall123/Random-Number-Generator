def main():
    import random

    print("Insert range of integers")
    a = int(input("Insert Low Range:\n"))
    b = int(input("Insert High Range:\n"))

    c = int(input("How many numbers do you want to generate?\n"))

    def function():
        x = random.randint(a,b)
        print (x)

    def repeat_fun(times, f, *args):
        for i in range(times): f(*args)
    
    repeat_fun(c,function)

while True:
    main()
    if input("Repeat the program? (Y/N):\n").strip().upper() != 'Y':
        break
