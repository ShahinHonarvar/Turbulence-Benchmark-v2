def gcf_two_nums(nums):
    num1 = nums[78]
    num2 = nums[93]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        smaller = min(num1, num2)
        while True:
            remainder = smaller % num1
            if remainder == 0:
                return num1
            num1 = smaller
            smaller = remainder