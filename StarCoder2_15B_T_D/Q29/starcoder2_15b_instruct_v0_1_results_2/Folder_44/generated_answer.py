def gcf_two_nums(nums):
    if len(nums) < 89:
        return None
    a = nums[56]
    b = nums[88]
    if a == 0:
        return b
    elif b == 0:
        return a
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a