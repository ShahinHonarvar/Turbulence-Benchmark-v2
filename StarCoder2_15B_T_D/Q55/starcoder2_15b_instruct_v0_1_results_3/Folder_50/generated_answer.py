def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        for j in range(i, i + n):
            sublist = numbers[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == 45:
                result.append(sublist)
    return result