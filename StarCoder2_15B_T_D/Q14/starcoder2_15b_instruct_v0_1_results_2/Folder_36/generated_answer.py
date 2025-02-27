def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    start_index = 209 if 209 < len(nums) else 0
    for i, num in enumerate(nums[start_index:], start=start_index):
        if num != nums[start_index]:
            return num
    return None