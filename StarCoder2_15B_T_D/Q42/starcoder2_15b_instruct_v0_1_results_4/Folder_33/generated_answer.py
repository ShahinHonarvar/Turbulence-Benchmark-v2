def prime_factors(nums):
    integer = nums[321]
    prime_factors = set()
    for i in range(2, int(integer ** 0.5) + 1):
        if integer % i == 0:
            prime_factors.add(i)
    return prime_factors