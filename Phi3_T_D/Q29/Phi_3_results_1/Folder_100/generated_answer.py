def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = nums[96]
    second_num = nums[32]
    return gcd(first_num, second_num)