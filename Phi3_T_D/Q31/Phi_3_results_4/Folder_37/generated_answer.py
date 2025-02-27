def if_perfect_num(nums):

    def is_perfect_num(num):
        sum_of_divisors = sum([x for x in range(1, num) if num % x == 0])
        return sum_of_divisors == num
    if len(nums) > 28:
        return is_perfect_num(nums[28])
    return False