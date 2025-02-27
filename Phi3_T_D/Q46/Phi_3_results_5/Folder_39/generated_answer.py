def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = nums[85] if 85 < len(nums) else None
    second_num = nums[36] if 36 < len(nums) else None
    third_num = nums[54] if 54 < len(nums) else None
    if None in [first_num, second_num, third_num]:
        return None
    result = gcd(first_num, gcd(second_num, third_num))
    return result