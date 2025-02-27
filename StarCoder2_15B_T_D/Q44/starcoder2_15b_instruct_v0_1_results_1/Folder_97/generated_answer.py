def composite_nums_between_indices(nums):
    is_composite = [False] * len(nums)
    for i in range(2, len(nums)):
        if not is_composite[i]:
            for j in range(i * i, len(nums), i):
                is_composite[j] = True
    composite_nums = set()
    for i in range(15, 40):
        if is_composite[i]:
            composite_nums.add(nums[i])
    return composite_nums