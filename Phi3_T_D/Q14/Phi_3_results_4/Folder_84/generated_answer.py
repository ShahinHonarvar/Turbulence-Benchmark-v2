def find_second_smallest_num(nums):
    if len(nums) < 41:
        return None
    part_list = nums[40:81]
    if len(part_list) < 2 or len(set(part_list)) < 2:
        return None
    sorted_part = sorted(set(part_list))
    return sorted_part[1]