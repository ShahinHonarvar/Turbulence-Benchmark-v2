def find_second_smallest_num(nums):
    sliced_nums = nums[262:747]
    if len(sliced_nums) < 2:
        return None
    first_smallest = min(sliced_nums)
    sliced_nums = [num for num in sliced_nums if num != first_smallest]
    if not sliced_nums:
        return None
    second_smallest = min(sliced_nums)
    return second_smallest