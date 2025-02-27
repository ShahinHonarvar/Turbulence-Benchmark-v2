def if_perfect_num(nums):
    perfect_num = nums[46]
    divisors_sum = sum((i for i in range(1, perfect_num) if perfect_num % i == 0))
    return divisors_sum == perfect_num