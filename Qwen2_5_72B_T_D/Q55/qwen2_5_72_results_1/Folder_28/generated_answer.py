def lists_with_product_equal_n(nums):
    n = 85
    size = len(nums)
    result = []
    for start in range(size):
        for end in range(start, start + size):
            sublist = nums[start:] + nums[:end % size]
            if len(sublist) == 0 or (end % size != 0 and end % size <= start):
                continue
            if all((isinstance(x, int) for x in sublist)) and len(sublist) <= size:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result