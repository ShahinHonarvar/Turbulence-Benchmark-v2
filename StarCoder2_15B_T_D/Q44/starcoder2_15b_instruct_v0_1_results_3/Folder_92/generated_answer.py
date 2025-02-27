def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(1, len(nums) - 1):
        is_composite = False
        for j in range(2, nums[i] // 2 + 1):
            if nums[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(nums[i])
    return composite_nums