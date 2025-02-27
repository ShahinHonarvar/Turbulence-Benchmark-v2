def if_perfect_num(nums):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i + n // i
        return s == n and n != 1
    return is_perfect(nums[2]) if len(nums) > 2 else False