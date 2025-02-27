def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:end]
            if len(sublist) < n:
                product = 1
                for num in sublist:
                    product *= num
                if product == 83:
                    result.append(sublist)
    return result