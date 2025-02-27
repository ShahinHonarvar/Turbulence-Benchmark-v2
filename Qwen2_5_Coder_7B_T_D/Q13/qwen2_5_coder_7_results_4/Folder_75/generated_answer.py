def find_second_largest_num(nums):
    if len(nums) < 58:
        return None
    sub_nums = nums[56:58]
    if len(sub_nums) < 2:
        return None
    largest = max(sub_nums)
    sub_nums.remove(largest)
    second_largest = max(sub_nums)
    return second_largest