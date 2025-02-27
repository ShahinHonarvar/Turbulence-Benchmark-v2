def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[69]
    num3 = nums[97]
    if num1 == num2 == num3:
        return num1
    for i in range(min(num1, num2, num3), 0, -1):
        if num1 % i == num2 % i == num3 % i == 0:
            return i
    return 1