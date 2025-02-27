def find_second_largest_num(nums):
    if 90 <= len(nums) <= 100:
        sublist = nums[90:100]
        sorted_sublist = sorted(sublist, reverse=True)
        unique_sorted = list(dict.fromkeys(sorted_sublist))
        if len(unique_sorted) >= 2:
            return unique_sorted[1]
    return None