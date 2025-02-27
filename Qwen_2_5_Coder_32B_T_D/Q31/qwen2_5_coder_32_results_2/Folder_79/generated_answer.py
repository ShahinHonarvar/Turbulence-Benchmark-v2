def if_perfect_num(numbers):
    if len(numbers) <= 63:
        return False
    n = numbers[63]
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i + n // i
    return s == n