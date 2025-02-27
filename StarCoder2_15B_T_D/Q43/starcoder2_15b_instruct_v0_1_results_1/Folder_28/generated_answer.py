def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 38 <= i <= 54:
            primes.append(num)
    return sorted(primes, reverse=True)