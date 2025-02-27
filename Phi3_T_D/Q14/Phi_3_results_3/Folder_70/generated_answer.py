def find_second_smallest_num(nums):
    relevant_nums = nums[35:50]
    if not relevant_nums:
        return None
    sorted_nums = sorted(relevant_nums)
    return sorted_nums[1] if len(sorted_nums) > 1 else None