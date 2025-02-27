def gcf_three_nums(nums):
    if len(nums) < 3:
        return None
    a = nums[693]
    b = nums[331]
    c = nums[668]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a