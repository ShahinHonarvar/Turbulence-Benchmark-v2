def prime_factors(nums):
    num = nums[194]
    for i in range(2, num + 1):
        if all((i % j != 0 for j in range(2, i))):
            if num % i == 0:
                yield i