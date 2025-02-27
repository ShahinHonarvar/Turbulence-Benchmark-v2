def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[20]
    smallest_num = min(num1, num2)
    for i in range(smallest_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i