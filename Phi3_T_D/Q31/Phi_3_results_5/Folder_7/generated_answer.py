def if_perfect_num(nums):
    if len(nums) <= 851:
        return False

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return is_perfect(nums[851])