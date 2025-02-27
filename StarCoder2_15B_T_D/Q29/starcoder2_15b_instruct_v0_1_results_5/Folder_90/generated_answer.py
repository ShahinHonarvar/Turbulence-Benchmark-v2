def gcf_two_nums(nums: list) -> int:
    num1 = nums[634]
    num2 = nums[585]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num1, num2)