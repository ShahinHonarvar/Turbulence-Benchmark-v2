def prime_factors(nums):
    num = nums[828]
    for i in range(2, num + 1):
        while num % i == 0:
            num /= i
    return i