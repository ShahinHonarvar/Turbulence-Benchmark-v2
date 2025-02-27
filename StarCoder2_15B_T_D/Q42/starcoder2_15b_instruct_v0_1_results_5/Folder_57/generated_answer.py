def prime_factors(nums):
    num = nums[92]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            num //= i
    return num