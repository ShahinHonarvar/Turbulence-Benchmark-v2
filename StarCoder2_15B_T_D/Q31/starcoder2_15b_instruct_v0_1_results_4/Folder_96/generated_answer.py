def if_perfect_num(nums):

    def divisors_sum(num):
        return sum((d for d in range(1, num) if num % d == 0))
    return divisors_sum(nums[47]) == nums[47]