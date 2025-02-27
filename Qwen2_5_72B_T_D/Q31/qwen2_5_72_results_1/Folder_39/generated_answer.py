def if_perfect_num(numbers):
    target = numbers[59]
    divisors_sum = sum((i for i in range(1, target) if target % i == 0))
    return divisors_sum == target