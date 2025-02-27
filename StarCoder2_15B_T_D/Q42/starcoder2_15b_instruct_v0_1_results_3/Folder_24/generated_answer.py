def prime_factors(nums):
    index = 74
    num = nums[index]
    for i in range(2, num + 1):
        while num % i == 0:
            num //= i
    return i