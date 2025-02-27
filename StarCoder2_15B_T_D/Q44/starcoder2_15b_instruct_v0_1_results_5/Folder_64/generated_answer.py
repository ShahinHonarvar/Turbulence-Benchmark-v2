def composite_nums_between_indices(nums):
    is_composite = lambda x: any((x % i == 0 for i in range(2, x)))
    return set(filter(is_composite, nums[0:5]))