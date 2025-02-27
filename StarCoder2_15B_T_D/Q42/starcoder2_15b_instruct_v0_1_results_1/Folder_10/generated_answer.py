def prime_factors(nums):
    num = nums[54]
    prime_factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return set(prime_factors)