def find_divisors_in_range(n):
    result = []
    for i in range(2, 8):
        if n % i == 0:
            result.append(i)
    return result