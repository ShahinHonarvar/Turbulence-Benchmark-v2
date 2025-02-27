def if_perfect_num(nums):
    if len(nums) < 68:
        return False
    num_to_check = nums[67]
    sum_of_divisors = 0
    for i in range(1, num_to_check):
        if num_to_check % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num_to_check