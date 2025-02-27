def if_perfect_num(nums):
    return is_perfect_num(nums[77])

def is_perfect_num(num):
    return sum((divisor for divisor in range(1, num) if num % divisor == 0)) == num