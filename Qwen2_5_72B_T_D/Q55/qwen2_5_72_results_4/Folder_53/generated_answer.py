def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -87
    result = []

    def find_sublists(start, end, product):
        if product == target_product:
            result.append(nums[start:end + 1])
        if product == 0 or abs(product) > abs(target_product):
            return
        for i in range(start, n + start):
            current_product = product * nums[i % n]
            find_sublists(i + 1, i, current_product)
    for i in range(n):
        find_sublists(i, i, 1)
    return result