def find_second_largest_num(nums):
    relevant_nums = nums[10:67]
    if len(set(relevant_nums)) < 2:
        return None
    second_largest = sorted(set(relevant_nums), reverse=True)[1]
    return second_largest