def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[69]
    num3 = nums[97]
    smallest_num = min(num1, num2, num3)
    for i in range(smallest_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i