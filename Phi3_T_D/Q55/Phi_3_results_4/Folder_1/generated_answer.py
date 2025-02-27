def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n, target_product = (len(circular_list), -51)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == target_product and i <= j - half_size(j) <= n - 1 - half_size(j):
                result.append(circular_list[i:j + 1])
            if product > target_product:
                break
    return result

def half_size(index):
    return index // 2