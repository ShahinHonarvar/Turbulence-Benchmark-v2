def if_perfect_num(nums):

    def is_perfect(n):
        total = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total == n
    return is_perfect(nums[95]) if len(nums) > 95 else False