def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = 48
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - n] if start + end > n else nums[start:start + end]
            if len(sublist) > 0 and all((isinstance(x, int) for x in sublist)) and (1 <= len(sublist) <= n):
                product = 1
                for num in sublist:
                    product *= num
                if product == target_product:
                    result.append(sublist)
    return result