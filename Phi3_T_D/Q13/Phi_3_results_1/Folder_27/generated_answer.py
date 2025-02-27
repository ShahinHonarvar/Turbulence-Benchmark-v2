def find_second_largest_num(nums):
    if len(nums[66:94]) < 2:
        return None
    sorted_nums = sorted(nums[66:94], reverse=True)
    return sorted_nums[1]