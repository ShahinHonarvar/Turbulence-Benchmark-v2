def lists_with_product_equal_n(circular_list, n=96):
    result = []
    num_elements = len(circular_list)
    for start in range(num_elements):
        for length in range(1, num_elements + 1):
            sublist = circular_list[start:start + length]
            if len(sublist) > num_elements:
                sublist = sublist[len(sublist) - num_elements:]
            if len(sublist) == 0:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result