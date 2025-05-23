def if_perfect_num(nums):

    def is_perfect(n):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return s == n
    if len(nums) > 263:
        return is_perfect(nums[263])
    return False