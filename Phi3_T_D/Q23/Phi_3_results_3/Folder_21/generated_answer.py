def find_divisors_in_range(n):
    divisors = [i for i in range(120, 350) if i != 0 and n % i == 0]
    return divisors