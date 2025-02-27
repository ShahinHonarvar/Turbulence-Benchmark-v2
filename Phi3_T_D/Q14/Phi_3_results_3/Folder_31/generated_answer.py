def find_second_smallest_num(nums):
    relevant_nums = nums[29:94]
    if len(relevant_nums) < 2:
        return None
    relevant_nums.sort()
    return relevant_nums[1]