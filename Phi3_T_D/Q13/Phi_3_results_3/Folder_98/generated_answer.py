def find_second_largest_num(nums):
    applicable_nums = nums[:7]
    unique_applicable_nums = sorted(set(applicable_nums), reverse=True)
    return unique_applicable_nums[1] if len(unique_applicable_nums) > 1 else None