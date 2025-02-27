def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i, num in enumerate(lst):
        if is_prime(num) and 14 <= i <= 68:
            primes.append(num)
    primes.sort(reverse=True)
    return primes