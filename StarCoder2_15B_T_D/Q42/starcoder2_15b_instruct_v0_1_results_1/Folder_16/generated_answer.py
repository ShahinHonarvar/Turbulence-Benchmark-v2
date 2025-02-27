def prime_factors(nums):
    num = nums[162]
    prime_factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i
    return set(prime_factors)