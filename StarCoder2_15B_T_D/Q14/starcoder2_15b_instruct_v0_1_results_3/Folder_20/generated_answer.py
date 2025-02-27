def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    list_length = len(sorted_nums)
    if list_length < 95:
        return None
    return sorted_nums[75 + 1]