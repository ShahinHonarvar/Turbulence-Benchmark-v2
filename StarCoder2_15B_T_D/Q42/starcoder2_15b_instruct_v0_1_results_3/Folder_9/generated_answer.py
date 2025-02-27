def prime_factors(nums):
    num = nums[24]
    for i in range(2, num + 1):
        if all((num % j != 0 for j in range(2, i))):
            return i