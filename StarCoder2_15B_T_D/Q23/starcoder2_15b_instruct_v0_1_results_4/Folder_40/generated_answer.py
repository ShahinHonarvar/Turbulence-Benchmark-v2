import math

def find_divisors_in_range(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i >= 1 and i <= 2:
                divisors.append(i)
            if i != num // i:
                if num // i >= 1 and num // i <= 2:
                    divisors.append(num // i)
    return divisors