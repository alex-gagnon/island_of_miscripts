def fizzbuzz(n):
    arr = []
    for num in range(1, n):
        if num % 3 == 0 and num % 5 == 0:
            arr.append("FizzBuzz")
        elif num % 3 == 0:
            arr.append("Fizz")
        elif num % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(num)
    return arr


if __name__ == '__main__':
    r = fizzbuzz(101)
    for i in r:
        print(i)
