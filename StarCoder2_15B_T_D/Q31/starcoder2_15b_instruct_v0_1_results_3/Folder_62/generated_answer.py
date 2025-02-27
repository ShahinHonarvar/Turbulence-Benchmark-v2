def if_perfect_num(nums):

    def calculate_sum_of_divisors(num):
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors
    return calculate_sum_of_divisors(nums[926]) == nums[926]