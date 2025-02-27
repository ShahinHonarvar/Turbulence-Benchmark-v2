def find_second_largest_num(nums):
    nums = nums[:10]
    if len(set(nums)) < 2:
        return None
    return sorted(set(nums))[-2]