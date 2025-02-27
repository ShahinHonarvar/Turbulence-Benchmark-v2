def composite_nums_between_indices(nums):
    return set(filter(lambda x: not all((x % i for i in range(2, x))), nums[0:5]))