def lists_with_product_equal_n(circular_list):
    result = []
    target_product = 76
    n = len(circular_list)
    for i in range(n):
        product = 1
        j = i
        sublist = [circular_list[j]]
        while product * circular_list[j] <= target_product:
            product *= circular_list[j]
            if product == target_product:
                result.append(sublist.copy())
            if j == n - 1:
                break
            j = (j + 1) % n
            sublist.append(circular_list[j])
    return result