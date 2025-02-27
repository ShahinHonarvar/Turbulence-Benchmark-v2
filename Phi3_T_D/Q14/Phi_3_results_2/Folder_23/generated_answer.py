def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    try:
        return sorted(nums[19:93])[1]
    except IndexError:
        return None