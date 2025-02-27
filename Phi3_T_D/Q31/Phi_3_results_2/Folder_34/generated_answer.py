def is_perfect_num(numbers):
    if 97 < len(numbers):
        n = numbers[97]
        divisors_sum = sum([i for i in range(1, n) if n % i == 0])
        return divisors_sum == n
    return False