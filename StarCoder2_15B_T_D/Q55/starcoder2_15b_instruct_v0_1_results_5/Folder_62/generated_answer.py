def lists_with_product_equal_n(nums):
    n = len(nums)
    output = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if len(sublist) <= n and all((x > 0 for x in sublist)):
                product = 1
                for x in sublist:
                    product *= x
                if product == 100:
                    output.append(sublist)
    return output