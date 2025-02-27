def composite_nums_between_indices(nums):
    return set(filter(lambda x: not all((x % i for i in range(2, int(x ** 0.5) + 1))), nums[50:201]))