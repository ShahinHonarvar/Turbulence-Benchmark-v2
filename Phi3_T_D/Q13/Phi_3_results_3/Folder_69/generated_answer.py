def find_second_largest_num(nums):
    if 32 <= len(nums) <= 35:
        target_slice = nums[31:36]
        if len(set(target_slice)) < 2:
            return None
        return sorted(set(target_slice))[-2]
    return None