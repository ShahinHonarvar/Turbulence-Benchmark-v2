def find_second_smallest_num(nums):
    if len(nums) > 3:
        return sorted(nums[:4])[1]
    return None