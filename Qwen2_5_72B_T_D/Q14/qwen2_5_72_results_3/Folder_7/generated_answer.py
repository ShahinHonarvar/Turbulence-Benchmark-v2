def find_second_smallest_num(nums):
    if len(nums) < 987 or len(nums) < 686:
        return None
    sub_list = nums[686:988]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]