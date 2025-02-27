def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    a = nums[0]
    b = nums[1]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a