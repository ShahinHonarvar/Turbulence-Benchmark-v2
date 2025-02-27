def if_perfect_num(nums):

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    if len(nums) > 20:
        num = nums[20]
        divisors = get_divisors(num)
        if sum(divisors) == num:
            return True
        else:
            return False
    else:
        return False