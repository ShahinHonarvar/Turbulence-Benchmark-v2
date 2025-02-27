def lists_with_product_equal_n(nums):
    target_product = 100
    n = len(nums)
    results = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - (n - start)]
            if len(sublist) <= n and all((isinstance(x, int) for x in sublist)) and (product := 1) and (all(((product := (product * x)) for x in sublist)) == target_product):
                results.append(sublist)
    return results