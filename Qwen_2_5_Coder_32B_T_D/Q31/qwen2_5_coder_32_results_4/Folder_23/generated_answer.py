def if_perfect_num(numbers):
    if len(numbers) <= 69:
        return False
    n = numbers[69]
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n