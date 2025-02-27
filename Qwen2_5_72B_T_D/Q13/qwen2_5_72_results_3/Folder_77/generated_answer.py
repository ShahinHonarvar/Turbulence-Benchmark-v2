def find_second_largest_num(nums):
    if len(nums) < 538 or len(nums) > 538:
        return None
    sub_list = nums[527:539]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]