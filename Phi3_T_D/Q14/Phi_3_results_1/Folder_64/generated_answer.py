def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    relevant_nums = sorted(set(nums[:5]))
    return relevant_nums[1] if len(relevant_nums) > 1 else None