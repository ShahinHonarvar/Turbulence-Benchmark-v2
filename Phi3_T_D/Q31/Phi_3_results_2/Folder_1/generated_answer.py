def if_perfect_num(numbers):
    try:
        value = sum((i for i in range(1, numbers[85]) if numbers[85] % i == 0))
        return value == numbers[85]
    except IndexError:
        return False