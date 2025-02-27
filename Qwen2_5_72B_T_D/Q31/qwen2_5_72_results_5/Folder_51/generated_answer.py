def if_perfect_num(nums):

    def is_perfect(n):
        sum = 1
        for i in range(2, n):
            if n % i == 0:
                sum += i
        return sum == n
    return is_perfect(nums[64]) if len(nums) > 64 else False