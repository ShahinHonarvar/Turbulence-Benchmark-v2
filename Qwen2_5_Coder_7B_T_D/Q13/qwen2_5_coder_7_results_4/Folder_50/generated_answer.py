def find_second_largest_num(nums):
    try:
        subset = nums[70:85]
        if len(subset) < 2:
            return None
        subset.sort()
        return subset[-2]
    except IndexError:
        return None