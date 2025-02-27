def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    subset = nums[:10]
    subset.sort()
    return subset[1]