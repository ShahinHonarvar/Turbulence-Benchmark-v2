def if_perfect_num(nums):

    def find_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    if find_divisors(nums[88]) == nums[88]:
        return True
    else:
        return False