def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    result = nums[1]
    for num in (nums[2], nums[7]):
        result = gcd(result, num)
    return result