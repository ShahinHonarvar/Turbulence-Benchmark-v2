def lists_with_product_equal_n(nums):
    n = 632
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums) + i):
            product *= nums[j % len(nums)]
            sublist.append(nums[j % len(nums)])
            if product == n:
                result.append(sublist.copy())
            elif product > n:
                break
    return result