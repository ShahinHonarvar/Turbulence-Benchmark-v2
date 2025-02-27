def find_divisors_in_range(n):
    return [i for i in range(586, 841) if i != 0 and n % i == 0]