def gcf_three_nums(nums):
    num1 = nums[693]
    num2 = nums[331]
    num3 = nums[668]
    min_num = min(num1, num2, num3)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i