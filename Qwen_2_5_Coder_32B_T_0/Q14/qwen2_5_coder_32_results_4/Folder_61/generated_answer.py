def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sub_list = nums[:8]
    sub_list.sort()
    return sub_list[1]