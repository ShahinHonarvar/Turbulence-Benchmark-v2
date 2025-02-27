def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 7:
        return nums[6]
    else:
        return None