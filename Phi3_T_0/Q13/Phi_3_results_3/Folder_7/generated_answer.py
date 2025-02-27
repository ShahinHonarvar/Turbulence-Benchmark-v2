def find_second_largest_num(nums):
    if len(nums) < 264:
        return None
    start, end = (661, 924)
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    return max(sub_list)