def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[99]) if numbers[99] % i == 0]) == numbers[99]