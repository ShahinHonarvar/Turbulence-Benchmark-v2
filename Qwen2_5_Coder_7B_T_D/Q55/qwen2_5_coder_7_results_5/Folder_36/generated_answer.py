def lists_with_product_equal_n(numbers):
    results = []
    n = 714
    length = len(numbers)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= numbers[j % length]
            if product == n:
                results.append(numbers[i:j % length + 1])
            elif product > n:
                break
    return results