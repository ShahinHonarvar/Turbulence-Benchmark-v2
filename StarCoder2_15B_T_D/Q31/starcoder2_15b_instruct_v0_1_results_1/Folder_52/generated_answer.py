def if_perfect_num(nums):

    def divisors(n):
        return [d for d in range(1, n) if n % d == 0]
    return sum(divisors(nums[478])) == nums[478]