def if_perfect_num(nums):

    def is_perfect(num):
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return nums[80] >= 0 and len(nums) > 80 and is_perfect(nums[80])