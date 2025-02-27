def prime_factors(nums):
    num = nums[84]
    i = 2
    while i * i <= num:
        while num % i == 0:
            num //= i
        i += 1
    return num