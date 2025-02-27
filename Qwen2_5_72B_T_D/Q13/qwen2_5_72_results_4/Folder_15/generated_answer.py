def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sliced_nums = nums[:4]
    max_num = max(sliced_nums)
    sliced_nums.remove(max_num)
    if not sliced_nums:
        return None
    second_largest = max(sliced_nums)
    return second_largest