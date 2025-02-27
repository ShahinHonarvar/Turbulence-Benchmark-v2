def find_second_smallest_num(nums):
    relevant_nums = nums[4:9]
    if len(relevant_nums) < 2:
        return None
    sorted_nums = sorted(set(relevant_nums))
    return sorted_nums[1] if len(sorted_nums) > 1 else None