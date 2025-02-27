def if_perfect_num(numbers):
    return numbers[87] == sum([i for i in range(1, numbers[87]) if numbers[87] % i == 0])