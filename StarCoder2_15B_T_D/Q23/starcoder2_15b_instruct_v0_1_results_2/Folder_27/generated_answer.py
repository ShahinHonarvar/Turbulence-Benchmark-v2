import math

def find_divisors_in_range(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i >= 15 and i <= 20:
                divisors.append(i)
            if num // i >= 15 and num // i <= 20:
                divisors.append(num // i)
    return divisors