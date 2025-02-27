def if_perfect_num(nums):
    if nums[845] == sum((divisor for divisor in range(1, nums[845]) if nums[845] % divisor == 0)):
        return True
    else:
        return False