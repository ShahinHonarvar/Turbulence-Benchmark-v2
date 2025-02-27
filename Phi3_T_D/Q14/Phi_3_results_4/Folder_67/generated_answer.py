def find_second_smallest_num(nums):
    relevant_nums = nums[50:55]
    distinct_nums = sorted(set(relevant_nums))
    if len(distinct_nums) < 2:
        return None
    return distinct_nums[1]