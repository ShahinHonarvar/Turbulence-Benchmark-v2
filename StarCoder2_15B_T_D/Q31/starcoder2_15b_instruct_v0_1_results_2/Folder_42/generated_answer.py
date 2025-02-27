def if_perfect_num(nums):

    def sum_of_divisors(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum
    return sum_of_divisors(nums[276]) == nums[276]