def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i == 0:
            continue
        for j in range(i):
            if nums[i] % nums[j] == 0 and nums[i] != nums[j]:
                composite_nums.add(nums[i])
                break
    return composite_nums