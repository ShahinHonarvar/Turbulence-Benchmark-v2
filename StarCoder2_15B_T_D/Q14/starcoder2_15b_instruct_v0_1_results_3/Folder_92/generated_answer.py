def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) > 1:
        return nums[1]
    return None