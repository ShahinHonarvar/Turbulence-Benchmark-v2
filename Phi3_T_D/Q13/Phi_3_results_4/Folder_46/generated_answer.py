def find_second_largest_num(nums):
    start, end = (30, 87)
    sliced_nums = nums[start:end + 1]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]