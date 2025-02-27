def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 23 <= i <= 59:
            primes.append(num)
    return sorted(primes, reverse=True)