def find_second_largest_num(nums):
    nums.sort()
    second_largest_index = len(nums) - 2
    if 15 <= second_largest_index <= 51:
        return nums[second_largest_index]
    else:
        return None