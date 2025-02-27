def if_perfect_num(numbers):
    if len(numbers) <= 51:
        return False
    n = numbers[51]
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s == n