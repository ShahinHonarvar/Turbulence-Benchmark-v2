def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 201:
        return nums[200]
    else:
        return None