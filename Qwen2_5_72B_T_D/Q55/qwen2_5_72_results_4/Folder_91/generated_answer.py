def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            elements = [nums[(start + i) % n] for i in range(length)]
            product = 1
            for element in elements:
                product *= element
                if product > 2:
                    break
            if product == 2:
                results.append(elements)
    return results