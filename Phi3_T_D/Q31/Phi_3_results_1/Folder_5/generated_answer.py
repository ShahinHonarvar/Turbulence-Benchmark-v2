def if_perfect_num(nums):
    index_67 = 67
    if index_67 >= len(nums):
        return False
    num = nums[index_67]
    divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    return sum(divisors) == num