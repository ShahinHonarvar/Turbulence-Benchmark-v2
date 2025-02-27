def if_perfect_num(nums):
    if not nums or nums[0] < 1:
        return False

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return is_perfect(nums[0])