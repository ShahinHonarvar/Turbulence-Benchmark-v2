def if_perfect_num(numbers):
    return sum((i for i in range(1, numbers[18]) if numbers[18] % i == 0)) == numbers[18] * 2 - numbers[18]