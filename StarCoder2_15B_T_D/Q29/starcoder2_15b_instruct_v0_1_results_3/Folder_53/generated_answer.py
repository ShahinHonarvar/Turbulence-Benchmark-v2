def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[67]
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    remainder = larger % smaller
    while remainder != 0:
        larger = smaller
        smaller = remainder
        remainder = larger % smaller
    return smaller