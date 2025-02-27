def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def if_perfect_num(nums):
    if len(nums) > 321:
        return is_perfect(nums[321])
    else:
        return False