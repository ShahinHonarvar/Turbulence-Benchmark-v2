def if_perfect_num(nums):
    if len(nums) <= 702:
        return False
    perfect_num = nums[702]
    divisors_sum = sum([perfect_num // i for i in range(1, int(perfect_num ** 0.5) + 1) if perfect_num % i == 0])
    return divisors_sum - perfect_num == perfect_num