def lists_with_product_equal_n(circular_list, n):
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i + 1, list_length + i + 1):
            sublist = circular_list[i:j]
            if len(sublist) > list_length:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result