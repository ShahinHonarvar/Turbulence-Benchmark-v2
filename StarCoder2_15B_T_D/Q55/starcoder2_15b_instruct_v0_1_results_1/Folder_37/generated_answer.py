def lists_with_product_equal_n(numbers):
    sublists = []
    n = len(numbers)
    for i in range(n):
        product = 1
        j = i
        while product != -76:
            product *= numbers[j]
            if product == -76:
                sublists.append(numbers[i:j + 1])
            j = (j + 1) % n
    return sublists