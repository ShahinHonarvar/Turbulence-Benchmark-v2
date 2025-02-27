def find_second_largest_num(nums):
    start, end = (min(62, len(nums) - 1), min(63, len(nums) - 1))
    sublist = nums[start:end + 1]
    unique_nums = sorted(set(sublist), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None