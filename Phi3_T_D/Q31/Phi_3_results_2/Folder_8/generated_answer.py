def if_perfect_num(nums):
    perfect_num = nums[49]
    divisors = [i for i in range(1, perfect_num) if perfect_num % i == 0]
    return sum(divisors) == perfect_num