def if_perfect_num(nums):
    if len(nums) < 55:
        return False
    n = nums[54]
    return n == sum((x for x in range(1, n) if n % x == 0))