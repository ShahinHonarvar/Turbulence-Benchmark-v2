def find_second_largest_num(nums):
    filtered_nums = nums[:4]
    if len(set(filtered_nums)) < 2:
        return None
    return sorted(set(filtered_nums))[-2]