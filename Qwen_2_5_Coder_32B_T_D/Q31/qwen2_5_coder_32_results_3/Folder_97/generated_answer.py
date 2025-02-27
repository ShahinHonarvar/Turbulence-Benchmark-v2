def if_perfect_num(nums):

    def is_perfect(n):
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    return is_perfect(nums[132]) if len(nums) > 132 else False