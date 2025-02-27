def composite_nums_between_indices(nums):
    composites = {num for num in nums[0:10] if any((num % i == 0 for i in range(2, num)))}
    return composites