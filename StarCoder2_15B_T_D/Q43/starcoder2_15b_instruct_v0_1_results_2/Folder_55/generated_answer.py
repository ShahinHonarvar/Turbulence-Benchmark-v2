def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 2 <= i <= 2:
            primes.append(num)
    return sorted(primes)