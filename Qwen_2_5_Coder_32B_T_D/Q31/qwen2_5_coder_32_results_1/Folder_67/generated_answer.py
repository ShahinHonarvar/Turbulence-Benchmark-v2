def if_perfect_num(numbers):
    if len(numbers) <= 43:
        return False
    n = numbers[43]
    return n == sum((x for x in range(1, n) if n % x == 0))