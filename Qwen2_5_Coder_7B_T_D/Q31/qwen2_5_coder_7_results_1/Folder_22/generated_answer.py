def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[72]) if numbers[72] % i == 0]) == numbers[72] and numbers[72] != 1