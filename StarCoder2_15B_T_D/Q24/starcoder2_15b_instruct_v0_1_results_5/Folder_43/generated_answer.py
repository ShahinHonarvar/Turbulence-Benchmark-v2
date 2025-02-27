import math

def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i >= 19 and i <= 69:
                sum += i
            if i != n // i:
                if n // i >= 19 and n // i <= 69:
                    sum += n // i
    return sum