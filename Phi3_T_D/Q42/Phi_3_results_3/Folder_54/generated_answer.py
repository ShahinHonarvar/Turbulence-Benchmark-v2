def prime_factors(nums):
    prime_factors_set = set()
    target_num = nums[50]
    factor = 2
    while factor * factor <= target_num:
        if target_num % factor:
            factor += 1
        else:
            target_num //= factor
            prime_factors_set.add(factor)
    if target_num > 1:
        prime_factors_set.add(target_num)
    return prime_factors_set