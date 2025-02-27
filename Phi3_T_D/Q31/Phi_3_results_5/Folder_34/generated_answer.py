def if_perfect_num(nums):
    if 97 < len(nums):
        number = nums[97]
        if number == sum([i for i in range(1, number) if number % i == 0]):
            return True
    return False