def find_second_largest_num(nums):
    if len(nums) < 81:
        return None
    sub_list = nums[40:81]
    sub_list.sort(reverse=True)
    return sub_list[1]