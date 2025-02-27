def lists_with_product_equal_n(nums):
    target_product = -938
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] if start + end <= n else nums[start:n] + nums[0:(start + end) % n]
            if len(sublist) <= n and all((isinstance(x, int) for x in sublist)) and (-938 == eval('*'.join(map(str, sublist)))):
                result.append(sublist)
    return result