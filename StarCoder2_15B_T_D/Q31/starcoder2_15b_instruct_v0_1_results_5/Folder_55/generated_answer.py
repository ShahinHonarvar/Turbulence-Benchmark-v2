def if_perfect_num(nums):
    target_num = nums[21]
    sum_of_divisors = 0
    for i in range(1, target_num):
        if target_num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == target_num:
        return True
    else:
        return False