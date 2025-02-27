def find_divisors_in_range(n):
    divisors = []
    for i in range(3, n + 1):
        if n % i == 0 and 3 <= i <= 8:
            divisors.append(i)
    return divisors