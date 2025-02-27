def find_primes_between_indices(nums):
    if len(nums) < 2:
        return []
    i, j = (1, 1)
    if i < 0 or j < 0 or j < i or (j >= len(nums)):
        return []
    primes = []
    for num in nums[i:j + 1]:
        is_prime = True
        for k in range(2, int(num ** 0.5) + 1):
            if num % k == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes