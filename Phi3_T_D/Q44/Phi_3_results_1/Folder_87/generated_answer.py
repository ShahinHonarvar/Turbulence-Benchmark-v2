def composite_nums_between_indices(nums):
    composites = {num for num in nums[43:52] if any((num % i == 0 and num != i for i in range(2, int(num ** 0.5) + 1)))}
    return composites