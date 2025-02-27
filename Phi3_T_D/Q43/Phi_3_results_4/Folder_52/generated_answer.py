def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start, end = (33, 59)
    primes = [lst[i] for i in range(start, end + 1) if is_prime(lst[i])]
    primes.sort(reverse=True)
    return primes