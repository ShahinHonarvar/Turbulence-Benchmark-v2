def if_perfect_num(nums):

    def is_perfect(num):
        return sum((divisor for divisor in range(1, num) if num % divisor == 0)) == num
    return is_perfect(nums[194])