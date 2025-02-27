def lists_with_product_equal_n(arr):
    if len(arr) < 1:
        return []
    target = -81
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            if product == target:
                result.append(arr[i:j + 1])
            if product == 0 or product > target:
                break
        if i == len(arr) - 1:
            break
    return result