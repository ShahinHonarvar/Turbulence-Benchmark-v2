def if_perfect_num(nums):
    if sum_of_divisors(nums[94]) == nums[94]:
        return True
    else:
        return False

def sum_of_divisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum