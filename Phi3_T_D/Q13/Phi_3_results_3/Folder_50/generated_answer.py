def find_second_largest_num(nums):
    if len(nums) < 15:
        return None
    max_num, second_max_num = sorted(nums[70:85], reverse=True)[:2]
    return second_max_num if len(sorted(nums[70:85])) > 1 else None