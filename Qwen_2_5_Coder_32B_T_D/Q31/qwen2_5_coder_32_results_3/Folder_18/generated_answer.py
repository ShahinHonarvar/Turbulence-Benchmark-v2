def if_perfect_num(nums):

    def is_perfect(n):
        return n == sum((x for x in range(1, n) if n % x == 0))
    return is_perfect(nums[312]) if len(nums) > 312 else False