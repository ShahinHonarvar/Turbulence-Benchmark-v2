def composite_nums_between_indices(nums):
    is_composite = lambda n: any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))
    nums_between_indices = [n for n in nums[0:10] if is_composite(n)]
    return set(nums_between_indices)