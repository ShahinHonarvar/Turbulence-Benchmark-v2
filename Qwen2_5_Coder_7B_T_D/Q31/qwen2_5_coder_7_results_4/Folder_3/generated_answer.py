def if_perfect_num(numbers):
    return numbers[100] == sum([i for i in range(1, numbers[100]) if numbers[100] % i == 0])