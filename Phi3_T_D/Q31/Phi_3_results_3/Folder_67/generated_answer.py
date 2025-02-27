def is_perfect_num(num):
    return num == sum([x for x in range(1, num) if num % x == 0])

def if_perfect_num(nums):
    try:
        return is_perfect_num(nums[43])
    except IndexError:
        return False