def gcf_three_nums(nums):
    num1 = nums[29]
    num2 = nums[53]
    num3 = nums[42]
    gcf1 = gcf(num1, num2)
    gcf2 = gcf(gcf1, num3)
    return gcf2

def gcf(num1, num2):
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