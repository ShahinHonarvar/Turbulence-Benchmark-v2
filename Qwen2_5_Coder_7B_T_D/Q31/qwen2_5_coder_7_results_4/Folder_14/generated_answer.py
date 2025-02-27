def if_perfect_num(numbers):
    return sum((numbers[17] // i for i in range(1, numbers[17]))) == numbers[17]