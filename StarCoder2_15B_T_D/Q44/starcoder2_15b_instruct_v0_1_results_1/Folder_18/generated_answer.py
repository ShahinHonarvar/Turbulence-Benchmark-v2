def composite_nums_between_indices(nums):
    return set((n for n in nums[25:88] if any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))))