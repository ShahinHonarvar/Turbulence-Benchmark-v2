def if_perfect_num(nums):

    def is_perfect_num(num):
        sum_of_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_factors += i
        return sum_of_factors == num
    return is_perfect_num(nums[78])