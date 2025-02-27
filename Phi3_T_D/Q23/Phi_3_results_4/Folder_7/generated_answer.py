def find_divisors_in_range(n):
    if n < 1:
        raise ValueError('Input must be a positive integer')
    divisors = []
    for i in range(469, 683):
        if n % i == 0:
            divisors.append(i)
    return divisors