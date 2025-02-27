def find_second_largest_num(nums):
    if len(nums) < 53:
        return None
    start = 533
    end = 605
    nums_slice = nums[start:end + 1]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort()
    return nums_slice[-2] if nums_slice[-2] != nums_slice[-1] else None