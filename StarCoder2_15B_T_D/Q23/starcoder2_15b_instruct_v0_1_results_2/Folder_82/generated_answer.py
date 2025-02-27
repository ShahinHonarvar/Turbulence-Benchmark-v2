def find_divisors_in_range(n):
    assert n > 0, 'The input must be a positive integer'
    divisors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            if 4 <= i <= 6:
                divisors.append(i)
    return divisors