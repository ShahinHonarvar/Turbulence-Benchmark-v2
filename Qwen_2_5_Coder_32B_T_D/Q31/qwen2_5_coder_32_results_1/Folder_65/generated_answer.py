def if_perfect_num(numbers):
    if len(numbers) <= 35:
        return False
    n = numbers[35]
    s = sum([i for i in range(1, n) if n % i == 0])
    return s == n