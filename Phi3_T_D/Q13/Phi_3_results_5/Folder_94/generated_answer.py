def find_second_largest_num(nums):
    try:
        sliced_nums = nums[28:41]
        sorted_nums = sorted(set(sliced_nums), reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    except IndexError:
        return None