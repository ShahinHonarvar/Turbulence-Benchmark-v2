def find_second_smallest_num(nums):
    if len(nums) <= 43:
        return None
    relevant_nums = sorted(nums[56:99])
    if len(relevant_nums) < 2:
        return None
    return relevant_nums[1]