def prime_factors(nums):
    num = nums[478]
    i = 2
    prime_factors = []
    while i * i <= num:
        if num % i == 0:
            prime_factors.append(i)
            num //= i
        else:
            i += 1
    prime_factors.append(num)
    return set(prime_factors)