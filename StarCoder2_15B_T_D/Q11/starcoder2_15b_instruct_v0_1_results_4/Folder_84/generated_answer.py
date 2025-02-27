def find_largest_num(nums):
    if len(nums) < 44:
        return None
    sliced_list = nums[43:87]
    largest = max(sliced_list)
    return largest