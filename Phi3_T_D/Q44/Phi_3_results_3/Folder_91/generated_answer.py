def composite_nums_between_indices(nums):
    return {n for n in nums[5:6] if any((n % i == 0 and n != i for i in range(2, n)))}