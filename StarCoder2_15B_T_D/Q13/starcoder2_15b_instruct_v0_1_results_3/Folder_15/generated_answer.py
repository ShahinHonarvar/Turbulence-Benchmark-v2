def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 3:
        return nums[1]
    else:
        return None