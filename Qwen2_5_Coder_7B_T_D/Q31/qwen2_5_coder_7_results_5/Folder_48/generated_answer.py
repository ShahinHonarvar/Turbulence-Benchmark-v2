def if_perfect_num(numbers):
    return sum((numbers[247] // i for i in range(1, numbers[247] // 2 + 1))) == numbers[247]