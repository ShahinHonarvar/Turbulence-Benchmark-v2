def if_perfect_num(nums):
    if nums[85] == sum((divisor for divisor in range(1, nums[85]) if nums[85] % divisor == 0)):
        return True
    else:
        return False