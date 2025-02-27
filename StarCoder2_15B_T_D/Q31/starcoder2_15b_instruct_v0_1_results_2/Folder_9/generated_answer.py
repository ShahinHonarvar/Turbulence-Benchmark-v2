def if_perfect_num(nums):
    num_to_check = nums[24]
    sum_of_divisors = 0
    for i in range(1, num_to_check + 1):
        if num_to_check % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num_to_check