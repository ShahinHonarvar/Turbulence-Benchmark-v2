def find_second_smallest_num(nums):
    start_index = 22
    end_index = 63
    unique_nums = sorted(set(nums[start_index:end_index + 1]))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]