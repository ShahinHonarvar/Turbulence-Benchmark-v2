def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    nums_slice = nums[:5]
    if len(set(nums_slice)) < 2:
        return None
    sorted_nums = sorted(nums_slice)
    return sorted_nums[1]