def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [x for i, x in enumerate(lst) if is_prime(x) and 424 <= i <= 552]
    return sorted(primes, reverse=True)