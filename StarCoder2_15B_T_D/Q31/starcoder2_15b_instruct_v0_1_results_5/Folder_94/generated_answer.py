def if_perfect_num(nums):
    num = nums[93]
    if num <= 0:
        return False
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    return sum_of_factors == num