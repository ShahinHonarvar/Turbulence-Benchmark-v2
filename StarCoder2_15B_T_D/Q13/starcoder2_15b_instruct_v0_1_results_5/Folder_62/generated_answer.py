def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    if len(nums) < 100:
        return nums[1]
    return nums[91:100][1]