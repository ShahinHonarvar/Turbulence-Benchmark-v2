def find_second_largest_num(nums):
    if len(nums[25:88]) < 2:
        return None
    sorted_nums = sorted(nums[25:88], reverse=True)
    return sorted_nums[1]