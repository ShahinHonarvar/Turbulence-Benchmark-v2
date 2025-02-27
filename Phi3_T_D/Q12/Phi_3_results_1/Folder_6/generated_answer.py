def find_smallest_num(nums):
    start_index = min(21, len(nums) - 1)
    end_index = min(97, len(nums) - 1) + 1
    return min(nums[start_index:end_index])