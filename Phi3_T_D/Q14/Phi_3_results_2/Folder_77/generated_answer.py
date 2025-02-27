def find_second_smallest_num(nums):
    if 639 <= len(nums) <= 975:
        unique_nums = set(nums[639:976])
        if len(unique_nums) < 2:
            return None
        unique_nums.remove(min(unique_nums))
        return min(unique_nums)
    return None