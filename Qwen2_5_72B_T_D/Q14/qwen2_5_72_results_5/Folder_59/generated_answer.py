def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    slice_nums = nums[:10]
    if len(set(slice_nums)) < 2:
        return None
    return sorted(slice_nums)[1]