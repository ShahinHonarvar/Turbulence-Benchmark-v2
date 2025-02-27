def lists_with_product_equal_n(numbers):
    n = len(numbers)
    numbers = numbers + numbers
    target_product = 6
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= numbers[j]
            if product == target_product:
                result.append(numbers[i:j + 1])
            elif product > target_product:
                break
    return result