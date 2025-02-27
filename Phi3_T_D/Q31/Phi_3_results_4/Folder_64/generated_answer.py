def if_perfect_num(nums):
    if len(nums) < 2:
        return False
    num = nums[1]
    sum_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_factors += i
            if i != num // i:
                sum_factors += num // i
    return sum_factors == num