def composite_nums_between_indices(nums):
    s = set()
    is_composite = lambda x: any((x % i == 0 for i in range(2, int(x ** 0.5) + 1)))
    for i in range(max(10, len(nums) - 1), min(101, len(nums))):
        if nums[i] > 1 and is_composite(nums[i]):
            s.add(nums[i])
    return s