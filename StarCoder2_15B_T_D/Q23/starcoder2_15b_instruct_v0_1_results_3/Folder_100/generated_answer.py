def find_divisors_in_range(num):
    if num <= 0:
        return []
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            if 11 <= i <= 41:
                divisors.append(i)
            else:
                continue
    return divisors