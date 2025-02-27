def if_perfect_num(numbers):
    return numbers[85] == sum([i for i in range(1, numbers[85]) if numbers[85] % i == 0])