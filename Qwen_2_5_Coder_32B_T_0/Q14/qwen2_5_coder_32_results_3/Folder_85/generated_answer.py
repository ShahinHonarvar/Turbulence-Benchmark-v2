def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    sub_list = nums[:7]
    sub_list.sort()
    return sub_list[1]