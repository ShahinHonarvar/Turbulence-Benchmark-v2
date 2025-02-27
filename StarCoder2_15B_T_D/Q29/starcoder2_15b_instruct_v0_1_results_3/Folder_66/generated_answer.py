def gcf_two_nums(nums):
    num1 = nums[86]
    num2 = nums[89]
    if num1 > num2:
        larger = num1
        smaller = num2
    else:
        larger = num2
        smaller = num1
    remainder = larger % smaller
    while remainder != 0:
        larger = smaller
        smaller = remainder
        remainder = larger % smaller
    return smaller