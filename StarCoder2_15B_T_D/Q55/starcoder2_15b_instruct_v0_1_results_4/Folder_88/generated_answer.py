def lists_with_product_equal_n(nums):
    n = -56
    result = []
    for i in range(len(nums)):
        window_size = 1
        while window_size <= len(nums):
            for j in range(i, i + window_size):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k % len(nums)]
                if product == n:
                    sublist = []
                    for k in range(i, j + 1):
                        sublist.append(nums[k % len(nums)])
                    result.append(sublist)
            window_size += 1
    return result