def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[410]) if numbers[410] % i == 0]) == numbers[410]