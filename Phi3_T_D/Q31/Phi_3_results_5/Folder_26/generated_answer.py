def if_perfect_num(numbers):
    if 222 < len(numbers):
        n = numbers[222]
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        return sum(divisors) == n
    return False