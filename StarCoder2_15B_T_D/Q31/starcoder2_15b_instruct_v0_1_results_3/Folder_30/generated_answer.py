def if_perfect_num(nums):

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    if get_divisors(nums[94]) == nums[94]:
        return True
    else:
        return False