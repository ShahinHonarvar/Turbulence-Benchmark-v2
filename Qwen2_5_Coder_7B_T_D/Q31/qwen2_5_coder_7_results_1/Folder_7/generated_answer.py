def if_perfect_num(numbers):
    return sum(numbers[851] == sum((i for i in range(1, numbers[851]) if numbers[851] % i == 0))) == 1