def find_second_largest_num(nums):
    if len(nums) < 6 or 28 not in range(len(nums)) or 32 not in range(len(nums)):
        return None
    target_slice = nums[28:33]
    distinct_numbers = sorted(set(target_slice))
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[-2]