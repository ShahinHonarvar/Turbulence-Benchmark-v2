def if_perfect_num(nums):

    def is_perfect(num):
        s = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                s += i + num // i
        return s == num
    return is_perfect(nums[126]) if len(nums) > 126 else False