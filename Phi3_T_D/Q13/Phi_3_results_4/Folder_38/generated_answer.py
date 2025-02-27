def find_second_largest_num(numbers_list):
    if len(numbers_list) < 42:
        return None
    trimmed_list = numbers_list[22:64]
    unique_nums = set(trimmed_list)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)