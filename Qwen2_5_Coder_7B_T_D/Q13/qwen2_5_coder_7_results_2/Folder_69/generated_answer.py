def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    sliced_nums = nums[32:36]
    if len(sliced_nums) < 2:
        return None
    largest = max(sliced_nums)
    sliced_nums.remove(largest)
    second_largest = max(sliced_nums)
    return second_largest