def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = circular_list[i:j]
            if len(sublist) > n:
                break
            if j > n:
                sublist = sublist + circular_list[:j - n]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
    return result