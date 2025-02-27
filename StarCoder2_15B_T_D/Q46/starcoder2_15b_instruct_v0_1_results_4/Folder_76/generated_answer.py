def gcf_three_nums(nums):
    num_876 = nums[876]
    num_203 = nums[203]
    num_100 = nums[100]
    common_factors = []
    for i in range(1, min(num_876, num_203, num_100) + 1):
        if num_876 % i == 0 and num_203 % i == 0 and (num_100 % i == 0):
            common_factors.append(i)
    return max(common_factors)