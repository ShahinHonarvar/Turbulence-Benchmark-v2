def gcf_three_nums(nums):
    num1 = nums[944]
    num2 = nums[814]
    num3 = nums[865]
    gcd = num1
    while num2 != 0:
        gcd = num2
        num2 = num1 % num2
        num1 = gcd
    while num3 != 0:
        gcd = num3
        num3 = num1 % num3
        num1 = gcd
    return gcd