def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[97]) if numbers[97] % i == 0]) == numbers[97]