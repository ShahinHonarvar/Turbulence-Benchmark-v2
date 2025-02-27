def find_divisors_in_range(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and i >= 39 and (i <= 43):
            divisors.append(i)
    return divisors