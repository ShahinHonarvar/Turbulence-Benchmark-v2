def composite_nums_between_indices(nums):
    return set(filter(lambda n: not all((n % i for i in range(2, int(n ** 0.5) + 1))), nums[21:98]))