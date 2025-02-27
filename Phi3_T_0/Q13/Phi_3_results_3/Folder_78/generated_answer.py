def find_second_largest_num(nums):
    if len(nums) < 8 or len(nums) > 10:
        return None
    start, end = (43, 51)
    sliced_nums = nums[start:end + 1]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]