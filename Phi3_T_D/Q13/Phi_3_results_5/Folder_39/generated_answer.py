def find_second_largest_num(nums):
    relevant_nums = nums[20:31]
    if len(relevant_nums) < 2:
        return None
    relevant_nums.sort()
    return relevant_nums[-2]