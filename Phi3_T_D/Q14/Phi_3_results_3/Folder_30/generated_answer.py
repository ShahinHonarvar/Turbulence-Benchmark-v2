def find_second_smallest_num(nums):
    relevant_nums = nums[26:53]
    if len(relevant_nums) >= 2:
        sorted_nums = sorted(relevant_nums)
        return sorted_nums[1]
    return None