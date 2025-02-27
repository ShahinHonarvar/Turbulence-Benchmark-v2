def find_divisors_in_range(n):
    divisors_in_range = [i for i in range(658, 869) if i != 0 and n % i == 0]
    return divisors_in_range