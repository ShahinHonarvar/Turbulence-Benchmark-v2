def find_second_largest_num(nums):
    slice_nums = nums[52:72]
    if len(slice_nums) < 2:
        return None
    largest = max(slice_nums)
    slice_nums.remove(largest)
    second_largest = max(slice_nums)
    return second_largest