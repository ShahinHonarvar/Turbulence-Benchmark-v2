def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[54]) if numbers[54] % i == 0]) == numbers[54]