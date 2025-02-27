def find_second_largest_num(nums):
    if len(nums[56:82]) < 2:
        return None
    subslice = sorted(nums[56:82], reverse=True)
    return subslice[1] if subslice[1] != subslice[0] else None