def find_second_smallest_num(nums):
    nums = nums[:3]
    if len(set(nums)) < 2:
        return None
    return sorted(set(nums))[1]