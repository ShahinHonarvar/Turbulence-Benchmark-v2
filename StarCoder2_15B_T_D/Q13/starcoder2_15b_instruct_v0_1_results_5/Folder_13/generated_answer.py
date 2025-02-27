def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 87:
        return nums[86]
    else:
        return None