def find_second_largest_num(nums):
    if len(nums[0:10]) < 2:
        return None
    first, second = sorted(set(nums[0:10]), reverse=True)[:2]
    return second