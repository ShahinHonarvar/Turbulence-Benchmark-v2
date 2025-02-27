def gcf_two_nums(nums):
    num1 = nums[25]
    num2 = nums[80]
    divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return max(divisors)