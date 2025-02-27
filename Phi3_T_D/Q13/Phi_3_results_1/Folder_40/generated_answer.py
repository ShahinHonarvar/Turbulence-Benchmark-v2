def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    sorted_nums = sorted(nums[:3])
    return sorted_nums[-2] if sorted_nums else None