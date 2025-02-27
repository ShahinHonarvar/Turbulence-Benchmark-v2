def if_perfect_num(nums):
    if not isinstance(nums, list) or len(nums) < 38:
        return False

    def is_perfect(n):
        sum_div = sum([i for i in range(1, n) if n % i == 0])
        return sum_div == n
    return is_perfect(nums[37])