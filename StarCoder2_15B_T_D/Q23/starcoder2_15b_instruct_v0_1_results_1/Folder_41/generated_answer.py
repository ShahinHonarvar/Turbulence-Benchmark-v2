def find_divisors_in_range(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0 and 2 <= i <= 4:
            divisors.append(i)
    return divisors