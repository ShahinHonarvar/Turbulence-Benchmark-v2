def gcf_two_nums(nums):
    num1 = nums[36]
    num2 = nums[54]
    if num1 > num2:
        larger = num1
        smaller = num2
    else:
        larger = num2
        smaller = num1
    while smaller != 0:
        remainder = larger % smaller
        larger = smaller
        smaller = remainder
    return larger