def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 2 or 100 >= len(nums):
        return None
    return nums[1]