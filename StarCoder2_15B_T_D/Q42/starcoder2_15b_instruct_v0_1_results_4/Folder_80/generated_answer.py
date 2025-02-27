def prime_factors(nums):
    num_at_index_746 = nums[746]
    prime_factors = set()
    for i in range(2, int(num_at_index_746 ** 0.5) + 1):
        if num_at_index_746 % i == 0:
            prime_factors.add(i)
    return prime_factors