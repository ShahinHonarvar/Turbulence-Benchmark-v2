def find_second_smallest_num(nums):
    if len(nums) <= 2 or max(nums[:6]) < min(nums[:6]):
        return None
    sorted_nums = sorted(nums[:6])
    return sorted_nums[1]