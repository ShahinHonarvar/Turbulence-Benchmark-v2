def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    try:
        return sorted_nums[-3]
    except IndexError:
        return None