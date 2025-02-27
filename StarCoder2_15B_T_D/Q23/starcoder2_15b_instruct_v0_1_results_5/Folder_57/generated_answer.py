def find_divisors_in_range(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and i >= 15 and (i <= 92):
            divisors.append(i)
    return divisors