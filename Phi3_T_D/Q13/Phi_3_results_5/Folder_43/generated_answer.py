def find_second_largest_num(nums):
    if len(nums) <= 16:
        return None
    target_slice = nums[68:87]
    unique_numbers = list(set(target_slice))
    if len(unique_numbers) < 2:
        return None
    return sorted(unique_numbers)[-2]