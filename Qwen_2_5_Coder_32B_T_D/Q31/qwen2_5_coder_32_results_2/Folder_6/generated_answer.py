def if_perfect_num(nums):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
        return s == n
    if len(nums) > 790:
        return is_perfect(nums[790])
    return False