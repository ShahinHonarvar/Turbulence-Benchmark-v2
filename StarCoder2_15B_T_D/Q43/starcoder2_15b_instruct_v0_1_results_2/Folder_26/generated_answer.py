def find_primes_between_indices(nums):
    if not isinstance(nums, list):
        raise TypeError('Input must be a list')
    primes = []
    for num in nums[23:49]:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes