def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    for start in range(size):
        product = 1
        i = start
        while i < size:
            product *= nums[i % size]
            if product == 47:
                result.append(nums[start:i + 1])
                if i + 1 < size:
                    i += 1
                else:
                    break
            elif product > 47:
                break
            i += 1
    return result