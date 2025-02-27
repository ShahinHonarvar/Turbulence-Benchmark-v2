def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[45]) if numbers[45] % i == 0]) == numbers[45]