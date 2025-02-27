def if_perfect_num(nums):
    index_46 = nums[46]
    divisor_sum = sum([(index_46 % i == 0) * (i if i != 1 else 0) for i in range(1, index_46 // 2 + 1)])
    return divisor_sum == index_46