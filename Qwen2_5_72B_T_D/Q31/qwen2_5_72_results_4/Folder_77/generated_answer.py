def if_perfect_num(numbers):
    target = numbers[985]
    sum_divisors = sum((i for i in range(1, target) if target % i == 0))
    return sum_divisors == target