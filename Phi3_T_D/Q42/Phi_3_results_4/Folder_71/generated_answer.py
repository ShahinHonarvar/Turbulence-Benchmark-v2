def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(integers):
    index_to_check = 78
    if index_to_check < len(integers):
        number = integers[index_to_check]
        factors = set()
        for i in range(2, number + 1):
            if is_prime(i) and number % i == 0:
                factors.add(i)
        return factors
    else:
        return 'No element at index 78'