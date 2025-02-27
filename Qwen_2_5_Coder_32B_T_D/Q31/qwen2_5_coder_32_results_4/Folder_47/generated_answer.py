def if_perfect_num(numbers):
    if 34 >= len(numbers):
        return False
    n = numbers[34]
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s == n and n != 1