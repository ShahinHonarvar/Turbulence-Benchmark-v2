def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 201:
        return nums[91]
    else:
        return None