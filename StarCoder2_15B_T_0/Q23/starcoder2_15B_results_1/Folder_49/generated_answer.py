def find_divisors_in_range(num):
    divisors = []
    for i in range(2, num + 1):
        if num % i == 0 and i >= 2 and (i <= 6):
            divisors.append(i)
    return divisors