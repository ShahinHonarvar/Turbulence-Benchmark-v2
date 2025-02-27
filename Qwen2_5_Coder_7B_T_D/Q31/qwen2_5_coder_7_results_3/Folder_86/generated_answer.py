def if_perfect_num(numbers):
    return sum((numbers[194] // i for i in range(1, numbers[194]))) == numbers[194] and numbers[194] != 1