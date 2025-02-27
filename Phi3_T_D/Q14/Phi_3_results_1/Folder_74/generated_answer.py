def find_second_smallest_num(nums):
    if 36 <= len(nums) <= 46:
        sublist = sorted(nums[36:47])
        unique_nums = sorted(list(set(sublist)))
        return unique_nums[1] if len(unique_nums) > 1 else None
    else:
        return None