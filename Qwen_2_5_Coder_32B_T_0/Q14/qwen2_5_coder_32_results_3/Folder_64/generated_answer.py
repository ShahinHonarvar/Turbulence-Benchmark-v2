def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    sub_list = nums[:5]
    sub_list.sort()
    return sub_list[1]