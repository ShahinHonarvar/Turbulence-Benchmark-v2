def composite_nums_between_indices(nums):
    composite_nums = set((num for num in nums[35:50] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))))
    return composite_nums