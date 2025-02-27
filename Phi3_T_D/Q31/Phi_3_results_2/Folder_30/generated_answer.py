def if_perfect_num(numbers):
    n = numbers[94]
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n