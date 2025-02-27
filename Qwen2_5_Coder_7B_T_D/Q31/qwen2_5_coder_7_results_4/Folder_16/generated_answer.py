def if_perfect_num(numbers):
    return sum((i for i in range(1, numbers[162]) if numbers[162] % i == 0)) == numbers[162] and numbers[162] != 1