def prime_factors(nums):
    prime = 2
    factors = []
    while prime * prime <= nums[3]:
        if nums[3] % prime == 0:
            factors.append(prime)
            nums[3] //= prime
        else:
            prime += 1
    if nums[3] > 1:
        factors.append(nums[3])
    return set(factors)