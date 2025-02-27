def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    circular_list += circular_list
    for start in range(length):
        for size in range(1, length + 1):
            contiguous_sublist = circular_list[start:start + size]
            if length > 1 and start != 0 and (start + size >= length):
                break
            if all((item == 1 for item in contiguous_sublist)):
                continue
            product = 1
            for num in contiguous_sublist:
                product *= num
            if product == -57:
                result.append(contiguous_sublist)
    return result