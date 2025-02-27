def find_second_largest_num(nums):
    if len(nums) < 51:
        return None
    sorted_nums = sorted(nums[14:64])
    unique_nums = {num for num in sorted_nums}
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]