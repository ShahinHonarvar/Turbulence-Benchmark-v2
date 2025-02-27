def find_divisors_in_range(num):
    return [i for i in range(58, 91) if num % i == 0]

def find_divisors_in_range_optimized(num):
    divisors = []
    for i in range(58, 91):
        if num % i == 0:
            divisors.append(i)
    return divisors