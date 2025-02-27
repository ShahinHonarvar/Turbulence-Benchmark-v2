def find_primes_between_indices(nums):
    primes = [num for i, num in enumerate(nums) if 19 <= i <= 71 and is_prime(num)]
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True