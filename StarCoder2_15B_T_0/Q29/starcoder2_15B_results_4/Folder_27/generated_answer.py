def gcf_two_nums(nums):
    num1 = nums[15]
    num2 = nums[40]
    smaller = min(num1, num2)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i