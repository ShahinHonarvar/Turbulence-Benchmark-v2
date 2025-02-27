def lists_with_product_equal_n(nums):

    def product_sublists(i, n, current_product, current_list, result):
        if current_product == -46:
            result.append(current_list.copy())
        if n == 0 or current_product * nums[i] < -46 or current_product * nums[i] > -46:
            return
        for j in range(n):
            current_product *= nums[(i + j) % len(nums)]
            current_list.append(nums[(i + j) % len(nums)])
            product_sublists((i + j + 1) % len(nums), n - j - 1, current_product, current_list, result)
            current_product /= nums[(i + j) % len(nums)]
            current_list.pop()
    result = []
    for i in range(len(nums)):
        product_sublists(i, len(nums), 1, [], result)
    return result