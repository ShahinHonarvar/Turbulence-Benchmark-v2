def find_second_largest_num(nums):
    start, end = (4, 4)
    if start == end and nums[start] is None:
        return None
    nums = nums[start:end + 1]
    if len(nums) == 1:
        return None
    nums.sort()
    unique_nums = list(set(nums))
    return None if len(unique_nums) == 1 else unique_nums[-2]