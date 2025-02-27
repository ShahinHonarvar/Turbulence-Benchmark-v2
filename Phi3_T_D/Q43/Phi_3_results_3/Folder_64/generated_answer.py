def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    start, end = (7, 9)
    primes = filter(is_prime, int_list[start:end + 1])
    return sorted(primes, reverse=True)