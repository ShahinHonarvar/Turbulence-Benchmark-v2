def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    if 0 < 1 <= len(lst) and is_prime(lst[1 - 1]):
        primes.append(lst[1 - 1])
    return sorted(primes)