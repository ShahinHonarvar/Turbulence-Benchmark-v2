def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 2 and 10 >= 0:
        return nums[1]
    else:
        return None