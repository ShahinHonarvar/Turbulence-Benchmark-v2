def is_perfect_num(numbers):
    if len(numbers) > 93 and all((isinstance(i, int) and i > 0 for i in numbers)):
        n = numbers[93]
        divisors_sum = sum([i for i in range(1, n) if n % i == 0])
        return divisors_sum == n
    return False