def find_divisors_in_range(num):
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if 2 <= i <= 4:
                divisors.append(i)
            if 2 <= num // i <= 4:
                divisors.append(num // i)
    return divisors