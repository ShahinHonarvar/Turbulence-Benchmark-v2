def find_second_smallest_num(nums):
    start, end = (62, 78)
    if end >= len(nums):
        end = len(nums) - 1
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    unique_nums = sorted(set(sub_list))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]