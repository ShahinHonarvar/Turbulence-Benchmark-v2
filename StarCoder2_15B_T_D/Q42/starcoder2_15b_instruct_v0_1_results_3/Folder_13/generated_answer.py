def prime_factors(nums):
    num = nums[126]
    prime_factors = []
    i = 2
    while i <= num:
        while num % i == 0:
            prime_factors.append(i)
            num //= i
        i += 1
    return set(prime_factors)