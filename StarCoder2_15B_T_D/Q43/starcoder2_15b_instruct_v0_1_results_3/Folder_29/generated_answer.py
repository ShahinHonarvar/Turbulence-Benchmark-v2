def find_primes_between_indices(nums):
    if len(nums) < 33:
        raise ValueError('The list must have at least 33 elements.')

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num):
            if 24 <= i <= 32:
                primes.append(num)
    if not primes:
        return []
    primes.sort(reverse=True)
    return primes