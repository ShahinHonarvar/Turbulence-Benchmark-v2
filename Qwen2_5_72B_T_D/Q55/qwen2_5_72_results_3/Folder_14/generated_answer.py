def lists_with_product_equal_n(nums):

    def helper(start, product, current):
        if product == -72:
            result.append(current[:])
        if product == 0 or abs(product) > 72:
            return
        for i in range(start, start + len(nums)):
            num = nums[i % len(nums)]
            if num == 0 and product != 1:
                break
            current.append(num)
            helper(i + 1, product * num, current)
            current.pop()
    result = []
    for i in range(len(nums)):
        helper(i, 1, [])
    return result