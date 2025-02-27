def if_perfect_num(nums):
    if len(nums) < 18:
        return False
    num = nums[17]
    s = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            s += i + num // i
    return s == num