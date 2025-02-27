def if_perfect_num(nums):
    perfect = lambda num: sum((i for i in range(1, num) if num % i == 0)) == num
    return perfect(nums[37]) if 37 < len(nums) else False