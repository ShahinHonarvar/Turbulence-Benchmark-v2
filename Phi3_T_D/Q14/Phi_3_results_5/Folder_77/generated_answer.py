def find_second_smallest_num(nums):
    if len(nums) < 975 - 639 + 1:
        return None
    indices = range(639, 976)
    relevant_nums = [nums[i] for i in indices]
    if len(set(relevant_nums)) < 2:
        return None
    relevant_nums.sort()
    return relevant_nums[1]