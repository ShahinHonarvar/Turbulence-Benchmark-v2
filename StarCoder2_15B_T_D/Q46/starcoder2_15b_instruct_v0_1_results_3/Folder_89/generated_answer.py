def gcf_three_nums(nums):
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]

    def find_gcf(a, b):
        if b == 0:
            return a
        else:
            return find_gcf(b, a % b)
    gcf = find_gcf(num1, num2)
    gcf = find_gcf(gcf, num3)
    return gcf