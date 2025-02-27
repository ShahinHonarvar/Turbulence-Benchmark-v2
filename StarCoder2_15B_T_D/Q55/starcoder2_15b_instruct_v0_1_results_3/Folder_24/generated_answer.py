def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            k = j % n
            sublist = nums[i:k + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -89:
                result.append(sublist)
    return result