def find_divisors_in_range(num):
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i >= 5 and i <= 8:
                divisors.append(i)
            if num // i >= 5 and num // i <= 8:
                divisors.append(num // i)
    return divisors