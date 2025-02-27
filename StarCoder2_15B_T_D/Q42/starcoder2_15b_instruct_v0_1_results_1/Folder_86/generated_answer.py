def prime_factors(nums):
    num = nums[194]
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    factors.append(num)
    return set(factors)