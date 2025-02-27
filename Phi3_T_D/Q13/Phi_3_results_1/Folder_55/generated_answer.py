def find_second_largest_num(nums):
    max_num = None
    second_max = None
    for i in range(max(0, len(nums) - 10)):
        if max_num is None or nums[i] > max_num:
            second_max = max_num
            max_num = nums[i]
        elif nums[i] > second_max and nums[i] < max_num:
            second_max = nums[i]
    return second_max