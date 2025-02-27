def find_second_largest_num(nums):
    if not 19 <= len(nums) <= 92:
        return None
    sorted_subset = sorted(nums[19:92], reverse=True)
    distinct_subset = list(dict.fromkeys(sorted_subset))
    return None if len(distinct_subset) < 2 else distinct_subset[1]