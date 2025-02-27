def if_perfect_num(nums):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return is_perfect(nums[40]) if len(nums) > 40 else False