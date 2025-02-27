def if_perfect_num(nums):
    if len(nums) > 77 and is_perfect(nums[77]):
        return True
    return False

def is_perfect(num):
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    return sum == num