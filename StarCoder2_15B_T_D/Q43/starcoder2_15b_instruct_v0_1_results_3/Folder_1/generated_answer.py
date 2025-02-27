def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = [num for i, num in enumerate(nums) if 87 <= i <= 89 and is_prime(num)]
    return sorted(primes)