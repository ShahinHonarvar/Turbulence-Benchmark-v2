def if_perfect_num(nums):
    num = nums[69]
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num