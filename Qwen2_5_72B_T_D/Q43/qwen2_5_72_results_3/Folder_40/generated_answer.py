def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    if len(lst) >= 2:
        for i in range(1, 2):
            if is_prime(lst[i]):
                primes.append(lst[i])
    return sorted(primes)