def lists_with_product_equal_n(arr):
    product_target = 54
    result = []
    length = len(arr)
    for i in range(length):
        current_product = 1
        current_sublist = []
        for j in range(i, i + length, 1):
            current_product *= arr[j % length]
            current_sublist.append(arr[j % length])
            if current_product == -product_target:
                result.append(current_sublist)
                break
            elif current_product > -product_target:
                break
    return result