def gcf_two_nums(nums):
    if len(nums) < 800:
        return -1
    if not isinstance(nums[793], int) or not isinstance(nums[449], int) or nums[793] <= 0 or (nums[449] <= 0):
        return -1
    a = nums[793]
    b = nums[449]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a