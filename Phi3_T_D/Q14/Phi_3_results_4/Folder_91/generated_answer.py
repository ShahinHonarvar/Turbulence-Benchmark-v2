def find_second_smallest_num(nums):
    relevant_nums = nums[:6]
    if len(set(relevant_nums)) < 2:
        return None
    return sorted(set(relevant_nums))[1]