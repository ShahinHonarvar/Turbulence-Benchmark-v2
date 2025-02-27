def lists_with_product_equal_n(nums):
    n = -9
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = []
        for j in range(i, len(nums) + i):
            if j == len(nums):
                j = 0
            sublist.append(nums[j])
            product *= nums[j]
            if product == n:
                result.append(sublist[:])
            elif product > n:
                break
    return result