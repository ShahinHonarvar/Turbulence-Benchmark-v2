def find_second_largest_num(nums):
    if len(nums) <= 538 - 527:
        return None
    sorted_section = sorted(nums[527:539], reverse=True)
    return sorted_section[1] if len(sorted_section) > 1 else None