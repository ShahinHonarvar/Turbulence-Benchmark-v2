def if_perfect_num(nums):

    def is_perfect(n):
        if n < 2:
            return False
        sum_divs = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_divs += i + n // i
        return sum_divs == n
    return is_perfect(nums[632]) if len(nums) > 632 else False