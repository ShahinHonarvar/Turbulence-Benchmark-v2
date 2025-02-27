def find_primes_between_indices(nums):
    """
    Find all prime numbers in the specified range and return them in
    descending order.
    """
    primes = []
    for num in nums[35:90]:
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)