def find_primes_between_indices(nums):
    primes = []
    for i in range(17, 80):
        if is_prime(nums[i - 1]):
            primes.append(nums[i - 1])
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True