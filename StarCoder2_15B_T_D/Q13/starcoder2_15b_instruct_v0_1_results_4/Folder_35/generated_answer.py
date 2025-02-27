def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums[30:49]) >= 2:
        return nums[30:49][1]
    else:
        return None