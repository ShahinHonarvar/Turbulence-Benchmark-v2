def find_divisors_in_range(n):
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i >= 2 and i <= 4:
                divisors.append(i)
            if i > 4:
                break
    return divisors