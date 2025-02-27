def if_perfect_num(nums):
    if 17 >= len(nums):
        return False
    num = nums[17]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num