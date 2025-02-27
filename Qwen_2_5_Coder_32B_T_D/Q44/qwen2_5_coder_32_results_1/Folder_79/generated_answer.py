def composite_nums_between_indices(nums):
    return set(nums[6:7]) & {num for num in range(4, max(nums) + 1) if any((num % i == 0 for i in range(2, num)))}