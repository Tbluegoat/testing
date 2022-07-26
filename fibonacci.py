from datetime import datetime

def get_fib(n:int):
    fib_array = [0, 1]
    while len(fib_array) < n:
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array[-1]

def get_fib2(n:int):
    if n == 1:
        return 0
    if n < 1:
        return "fuck you"
    num1 = 0
    num2 = 1
    counter = 2
    while counter < n:
        temp = num1
        num1 = num2
        num2 = temp + num2
        counter += 1
    return num2


if __name__ == "__main__":
    print("expecting get_fib(4) to be 2", get_fib2(4) == 2)
    print("expecting get_fib(4) to be 2", get_fib2(1) == 0)
    print("expecting get_fib(4) to be 2", get_fib2(2) == 1)
    print("expecting get_fib(5) to be 3", get_fib2(5) == 3)
    print("expecting get_fib(6) to be 5", get_fib2(6) == 5)
    print("expecting get_fib(7) to be 8", get_fib2(7) == 8)
    
    time = datetime.now()
    get_fib2(100000)
    print(datetime.now() - time)
    get_fib2(1000000)
    print(datetime.now() - time)

    # time = datetime.now()
    # get_fib(100000)
    # print(datetime.now() - time)
    # get_fib(200000)
    # print(datetime.now() - time)