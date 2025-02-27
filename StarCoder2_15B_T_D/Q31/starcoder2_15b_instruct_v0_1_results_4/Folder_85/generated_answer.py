def if_perfect_num(nums):

    def is_perfect_num(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return is_perfect_num(nums[23])