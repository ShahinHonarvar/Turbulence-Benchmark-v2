def find_second_smallest_num(nums):
    if len(nums) < 13:
        return None
    sliced_nums = nums[6:7]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]