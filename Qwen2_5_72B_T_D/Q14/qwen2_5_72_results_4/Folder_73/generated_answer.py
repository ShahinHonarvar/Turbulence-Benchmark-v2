def find_second_smallest_num(nums):
    if len(nums) < 98 or len(set(nums[59:98])) < 2:
        return None
    sub_list = nums[59:98]
    sub_list.sort()
    return sub_list[1]