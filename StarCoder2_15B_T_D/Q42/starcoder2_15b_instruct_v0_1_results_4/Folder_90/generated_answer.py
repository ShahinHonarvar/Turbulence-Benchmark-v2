def prime_factors(nums):
    num = nums[263]
    factors = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num //= i
        else:
            i += 1
    factors.append(num)
    return set(factors)