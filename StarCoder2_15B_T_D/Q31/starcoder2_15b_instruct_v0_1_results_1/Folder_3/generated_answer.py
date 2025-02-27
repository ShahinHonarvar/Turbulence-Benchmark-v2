def if_perfect_num(nums):

    def get_divisors_sum(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum
    return get_divisors_sum(nums[100]) == nums[100]