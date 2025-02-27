def gcf_two_nums(nums):
    if not isinstance(nums, list) or len(nums) < 5:
        return None
    a = nums[4]
    b = nums[0]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a