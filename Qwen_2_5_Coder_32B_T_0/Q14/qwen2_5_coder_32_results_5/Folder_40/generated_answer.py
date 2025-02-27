def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    sub_list = nums[:3]
    sub_list.sort()
    return sub_list[1]