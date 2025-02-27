def prime_factors(nums):
    num = nums[64]
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num