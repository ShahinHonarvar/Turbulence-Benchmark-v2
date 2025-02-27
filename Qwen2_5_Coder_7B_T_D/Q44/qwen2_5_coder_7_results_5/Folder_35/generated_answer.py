def composite_nums_between_indices(nums):
    return {num for num in nums[28:33] if not all((num % i for i in range(2, int(num ** 0.5) + 1)))}