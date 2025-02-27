def if_perfect_num(numbers):
    if len(numbers) > 85:
        n = numbers[85]
        divisors = [x for x in range(1, n) if n % x == 0]
        return sum(divisors) == n
    return False