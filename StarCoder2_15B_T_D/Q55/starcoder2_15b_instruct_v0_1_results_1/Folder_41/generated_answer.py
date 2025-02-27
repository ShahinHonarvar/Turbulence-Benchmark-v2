def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = numbers[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -20:
                result.append(sublist)
    return result