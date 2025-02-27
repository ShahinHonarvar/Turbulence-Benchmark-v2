def if_perfect_num(nums):

    def divisors_sum(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors)
    return divisors_sum(nums[68]) == nums[68]