def if_perfect_num(nums):
    if len(nums) < 4:
        return False
    num = nums[3]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num