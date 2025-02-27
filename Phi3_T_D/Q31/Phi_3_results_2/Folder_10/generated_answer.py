def if_perfect_num(nums):
    index_of_interest = 54
    if index_of_interest < len(nums):
        num = nums[index_of_interest]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False