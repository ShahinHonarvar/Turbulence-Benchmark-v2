def find_second_smallest_num(nums):
    nums_slice = nums[55:100]
    nums_slice.sort()
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]