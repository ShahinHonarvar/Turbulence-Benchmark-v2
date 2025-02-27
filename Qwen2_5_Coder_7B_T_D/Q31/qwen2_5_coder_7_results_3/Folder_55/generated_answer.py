def if_perfect_num(numbers):
    return numbers[21] == sum([i for i in range(1, numbers[21]) if numbers[21] % i == 0])