def prime_factors(nums):
    if len(nums) < 96:
        raise ValueError('List must contain at least 96 elements')
    num = nums[95]
    i = 2
    while i * i <= num:
        if num % i == 0:
            num = num // i
        else:
            i += 1
    return num