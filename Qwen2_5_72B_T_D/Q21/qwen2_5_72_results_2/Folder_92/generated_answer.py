def all_ints_div_by_num(nums):
    result = []
    if nums and len(nums) > 0 and (nums[0] % 1 == 0):
        result.append(nums[0])
    return result