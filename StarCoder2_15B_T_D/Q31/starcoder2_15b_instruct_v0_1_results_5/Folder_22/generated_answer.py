def if_perfect_num(nums):

    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    if sum(get_divisors(nums[72])) == nums[72]:
        return True
    else:
        return False