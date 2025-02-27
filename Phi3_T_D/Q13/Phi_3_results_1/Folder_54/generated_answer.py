def find_second_largest_num(nums):
    start_ind, end_ind = (34, 55)
    relevant_nums = nums[start_ind:end_ind + 1]
    if len(relevant_nums) >= 2:
        relevant_nums.sort()
        return relevant_nums[-2]
    return None