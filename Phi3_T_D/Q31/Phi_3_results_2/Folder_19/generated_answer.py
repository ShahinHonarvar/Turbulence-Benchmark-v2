def if_perfect_num(nums):
    if len(nums) <= 13:
        return False

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum += i
                if i != n // i:
                    sum += n // i
        return sum == n
    return is_perfect(nums[13])