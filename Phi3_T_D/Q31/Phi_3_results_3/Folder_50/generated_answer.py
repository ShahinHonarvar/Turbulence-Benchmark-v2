def if_perfect_num(numbers):
    divisors_sum = sum((i for i in range(1, numbers[40] // 2 + 1) if numbers[40] % i == 0))
    return divisors_sum == numbers[40]