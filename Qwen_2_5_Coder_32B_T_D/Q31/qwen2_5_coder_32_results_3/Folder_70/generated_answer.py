def if_perfect_num(numbers):
    if len(numbers) > 845:
        n = numbers[845]
        return n == sum((i for i in range(1, n) if n % i == 0))
    return False