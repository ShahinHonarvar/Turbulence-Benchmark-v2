def lists_with_product_equal_n(nums):
    target_product = 5
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            if j > n - i:
                sub_list = nums[i:] + nums[:j - (n - i)]
            else:
                sub_list = nums[i:i + j]
            if sub_list and (product := 1) and (all(((product := (product * x)) for x in sub_list)) == target_product):
                result.append(sub_list)
    return result