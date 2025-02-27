def find_divisors_in_range(num):
    if num <= 0:
        return []
    divisors = []
    for divisor in range(57, 87):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors