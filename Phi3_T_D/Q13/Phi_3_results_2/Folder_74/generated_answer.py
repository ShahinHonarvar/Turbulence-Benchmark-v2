def find_second_largest_num(nums):
    if 17 <= len(nums) <= 78:
        relevant_nums = nums[17:79]
        unique_nums = set(relevant_nums)
        if len(unique_nums) < 2:
            return None
        else:
            unique_nums.remove(max(unique_nums))
            return max(unique_nums)
    else:
        return None