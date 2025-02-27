def find_second_largest_num(nums):
    if 661 <= len(nums) <= 924:
        sorted_nums = sorted(nums[660:925], reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    return None