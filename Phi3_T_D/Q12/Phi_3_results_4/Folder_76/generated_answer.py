def find_smallest_num(nums):
    start_index = 246
    end_index = 750
    smallest_num = nums[start_index] if 0 <= start_index < len(nums) else float('inf')
    for i in range(start_index + 1, end_index + 1):
        if 0 <= i < len(nums) and nums[i] < smallest_num:
            smallest_num = nums[i]
    return smallest_num