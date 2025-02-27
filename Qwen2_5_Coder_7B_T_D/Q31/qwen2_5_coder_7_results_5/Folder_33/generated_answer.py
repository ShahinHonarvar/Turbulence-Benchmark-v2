def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[321]) if numbers[321] % i == 0]) == numbers[321]