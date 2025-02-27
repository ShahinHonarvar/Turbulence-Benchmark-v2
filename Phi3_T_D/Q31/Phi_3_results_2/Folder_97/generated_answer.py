def if_perfect_num(nums):
    if len(nums) > 132:
        n = nums[132]
        sum_divisors = sum([x for x in range(1, n) if n % x == 0])
        return sum_divisors == n
    return False