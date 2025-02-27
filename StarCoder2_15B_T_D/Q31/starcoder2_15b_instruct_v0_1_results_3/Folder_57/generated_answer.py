def if_perfect_num(nums):

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    divisors = get_divisors(nums[92])
    return sum(divisors) == nums[92]