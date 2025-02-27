def if_perfect_num(nums):
    return is_perfect(nums[746]) if len(nums) > 746 else False

def is_perfect(number):
    sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
    return sum_of_divisors == number