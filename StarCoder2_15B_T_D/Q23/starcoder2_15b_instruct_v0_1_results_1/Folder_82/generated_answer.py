def find_divisors_in_range(num):
    if num < 1:
        return []
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and i >= 4 and (i <= 6):
            divisors.append(i)
    return divisors