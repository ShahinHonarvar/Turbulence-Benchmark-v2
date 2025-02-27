def if_perfect_num(nums):
    num = nums[34]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        return True
    else:
        return False