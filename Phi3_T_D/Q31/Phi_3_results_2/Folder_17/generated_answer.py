def if_perfect_num(nums):
    if len(nums) <= 632:
        return False
    num = nums[632]
    divisors_sum = sum([x for x in range(1, num) if num % x == 0])
    return divisors_sum == num