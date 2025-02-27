def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers) + 1):
            sublist = numbers[i:j]
            product = 1
            for n in sublist:
                product *= n
            if product == -93:
                result.append(sublist)
    return result