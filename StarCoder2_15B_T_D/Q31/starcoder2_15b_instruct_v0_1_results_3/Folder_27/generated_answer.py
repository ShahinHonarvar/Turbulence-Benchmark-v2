def if_perfect_num(nums):

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    if sum(get_divisors(nums[56])) == nums[56]:
        return True
    else:
        return False