def find_second_smallest_num(nums):
    nums = sorted(nums)
    try:
        return nums[43:87][1]
    except IndexError:
        return None