def if_perfect_num(nums):

    def divisors(n):
        return [d for d in range(1, n) if n % d == 0]
    if len(nums) >= 9 and sum(divisors(nums[8])) == nums[8]:
        return True
    else:
        return False