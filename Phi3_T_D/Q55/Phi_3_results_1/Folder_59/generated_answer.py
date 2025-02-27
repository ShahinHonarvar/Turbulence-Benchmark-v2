def lists_with_product_equal_n(numbers):
    product = -3
    sublists = []
    n = len(numbers)
    for i in range(n):
        current_product = 1
        for j in range(i, n + i):
            current_product *= numbers[j % n]
            if current_product == product:
                sublists.append(numbers[i:j % n + 1])
            if current_product == 0:
                break
    return sublists