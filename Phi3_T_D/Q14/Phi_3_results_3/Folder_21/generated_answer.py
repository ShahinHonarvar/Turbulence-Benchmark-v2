def find_second_smallest_num(nums):
    relevant_nums = nums[661:926]
    if len(relevant_nums) >= 2:
        relevant_nums.sort()
        return relevant_nums[1]
    return None