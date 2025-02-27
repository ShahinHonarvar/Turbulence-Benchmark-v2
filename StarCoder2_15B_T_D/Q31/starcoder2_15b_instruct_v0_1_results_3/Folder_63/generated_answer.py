def if_perfect_num(nums):
    num = nums[57]
    sum_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num