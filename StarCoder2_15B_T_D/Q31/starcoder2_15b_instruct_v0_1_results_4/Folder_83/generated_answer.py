def if_perfect_num(nums):

    def is_perfect(num):
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div == num
    return is_perfect(nums[95])