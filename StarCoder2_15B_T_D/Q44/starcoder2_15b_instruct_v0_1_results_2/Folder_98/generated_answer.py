def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(1, 7):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    composite_nums.add(nums[i])
                    break
    return composite_nums