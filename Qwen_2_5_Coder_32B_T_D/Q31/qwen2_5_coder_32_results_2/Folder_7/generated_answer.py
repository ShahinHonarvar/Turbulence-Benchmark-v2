def if_perfect_num(numbers):
    if len(numbers) < 852:
        return False
    n = numbers[851]
    s = sum((i for i in range(1, n) if n % i == 0))
    return s == n