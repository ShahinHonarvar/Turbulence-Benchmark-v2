def if_perfect_num(numbers):
    if len(numbers) < 16:
        return False
    n = numbers[15]
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n