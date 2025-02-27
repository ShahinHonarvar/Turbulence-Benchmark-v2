def prime_factors(nums):
    num = nums[16]
    prime_factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            prime_factors.append(i)
            num //= i
        else:
            i += 1
    return set(prime_factors)