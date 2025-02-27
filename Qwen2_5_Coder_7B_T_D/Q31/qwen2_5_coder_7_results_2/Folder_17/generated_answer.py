def if_perfect_num(numbers):
    return sum((numbers[632] // i for i in range(1, numbers[632]))) == numbers[632] - 1