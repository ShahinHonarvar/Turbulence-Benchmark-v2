def find_primes_between_indices(nums):
    """Finds all prime numbers between indices 13 and 68 in a list of integers."""
    primes = []
    for i in range(13, 69):
        num = nums[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes