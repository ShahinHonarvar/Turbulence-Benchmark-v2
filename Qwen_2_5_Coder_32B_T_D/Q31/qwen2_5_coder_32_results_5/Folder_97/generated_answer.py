def if_perfect_num(nums):

    def is_perfect(n):
        sumf = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sumf += i
                if i != n // i:
                    sumf += n // i
        return sumf == n
    return is_perfect(nums[132]) if len(nums) > 132 else False