def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i == 0:
            continue
        for j in range(2, nums[i] // 2 + 1):
            if nums[i] % j == 0:
                composite_nums.add(nums[i])
                break
    return composite_nums