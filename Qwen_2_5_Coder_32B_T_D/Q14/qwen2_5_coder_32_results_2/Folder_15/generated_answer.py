def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    sub_list = nums[:4]
    sub_list.sort()
    return sub_list[1]