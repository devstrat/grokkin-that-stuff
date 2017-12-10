def fizzbuzz(num: int):
    return 'Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or num


if __name__ == '__main__':
    for item in range(1, 101):
        print(fizzbuzz(item))
