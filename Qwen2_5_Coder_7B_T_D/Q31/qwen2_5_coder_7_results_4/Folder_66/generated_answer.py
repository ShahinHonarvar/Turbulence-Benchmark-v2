def if_perfect_num(numbers):
    return sum([1 for i in range(1, numbers[42]) if numbers[42] % i == 0]) == numbers[42]