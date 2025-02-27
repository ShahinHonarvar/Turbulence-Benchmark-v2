def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 101:
        return nums[81]
    else:
        return None