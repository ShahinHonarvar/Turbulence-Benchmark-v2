def find_second_smallest_num(nums):
    selected_nums = nums[68:87]
    if len(selected_nums) < 2:
        return None
    sorted_nums = sorted(selected_nums)
    return sorted_nums[1]