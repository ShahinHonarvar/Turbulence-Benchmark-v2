def find_second_smallest_num(nums):
    if not nums or len(nums) < 2:
        return None
    nums.sort()
    if len(nums) < 64:
        return None
    return nums[22]