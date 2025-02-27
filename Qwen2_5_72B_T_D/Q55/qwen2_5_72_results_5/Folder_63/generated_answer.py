def lists_with_product_equal_n(nums):
    target_product = 96
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result