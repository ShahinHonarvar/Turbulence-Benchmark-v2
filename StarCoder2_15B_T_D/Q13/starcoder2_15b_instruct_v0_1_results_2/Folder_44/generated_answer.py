def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    for i, num in enumerate(sorted_nums):
        if i >= 13 and i <= 68:
            return num
    return None