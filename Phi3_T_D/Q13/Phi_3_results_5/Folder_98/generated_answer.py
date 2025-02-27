def find_second_largest_num(nums):
    if len(nums[:7]) < 2:
        return None
    first, second = sorted(set(nums[:7]))[-2:]
    return second