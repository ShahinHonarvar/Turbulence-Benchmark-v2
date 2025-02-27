def find_second_smallest_num(numbers):
    unique_nums = sorted(set(numbers))
    return unique_nums[1] if len(unique_nums) > 1 else None