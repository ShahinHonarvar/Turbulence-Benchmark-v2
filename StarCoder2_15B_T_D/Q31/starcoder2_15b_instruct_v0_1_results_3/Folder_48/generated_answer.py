def if_perfect_num(nums):
    if nums[247] == sum((divisor for divisor in range(1, nums[247]) if nums[247] % divisor == 0)):
        return True
    else:
        return False