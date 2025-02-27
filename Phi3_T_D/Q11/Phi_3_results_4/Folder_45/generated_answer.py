def find_largest_num(nums):
    try:
        return max(nums[30:31])
    except IndexError:
        return None