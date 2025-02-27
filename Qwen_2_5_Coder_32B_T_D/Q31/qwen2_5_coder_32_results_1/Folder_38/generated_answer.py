def if_perfect_num(numbers):
    if len(numbers) < 39:
        return False
    n = numbers[38]
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n