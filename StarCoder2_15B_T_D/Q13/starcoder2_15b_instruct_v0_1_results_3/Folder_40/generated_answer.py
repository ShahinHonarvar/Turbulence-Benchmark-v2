def find_second_largest_num(nums):
    largest_idx = nums.index(max(nums[:3]))
    second_largest_idx = None
    for i, num in enumerate(nums[:3]):
        if i != largest_idx and (second_largest_idx is None or num > nums[second_largest_idx]):
            second_largest_idx = i
    return nums[second_largest_idx] if second_largest_idx is not None else None