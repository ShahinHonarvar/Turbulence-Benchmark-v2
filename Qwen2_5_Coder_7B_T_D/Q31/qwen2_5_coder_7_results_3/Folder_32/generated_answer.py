def if_perfect_num(nums):
    if len(nums) > 849:
        num = nums[849]
        sum_div = sum([i for i in range(1, num) if num % i == 0])
        return sum_div == num
    return False