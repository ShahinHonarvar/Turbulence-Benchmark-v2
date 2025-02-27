def circular_product(ints, start, end, target):
    product = 1
    for i in range(start, end):
        product *= ints[i % len(ints)]
    return product

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(len(circular_list)):
            if circular_product(circular_list, i, j, -51):
                if not result or result[-1] != circular_list[i:j + 1]:
                    result.append(circular_list[i:j + 1])
    return result