def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    product_result = []
    for i in range(size):
        for j in range(i + 1, size + i):
            product = 1
            if j <= size:
                sublist = circular_list[i:j]
                if j > i:
                    sublist += circular_list[:j - i]
                product = product_result(sublist)
                if product == -1:
                    product_result.append(sublist)
    return product_result

def product_result(sublist):
    product = 1
    for number in sublist:
        product *= number
    return product