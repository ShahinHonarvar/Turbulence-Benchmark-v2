def lists_with_product_equal_n(nums):
    target_product = 51
    sublists = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == target_product:
                sublists.append(nums[i:index + 1])
            if product > target_product:
                break
    return sublists