def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 538:
        return None
    return nums[527]