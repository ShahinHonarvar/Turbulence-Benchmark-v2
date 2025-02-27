def circular_product(lst, start, end):
    total = 1
    while end != start:
        total *= lst[end]
        end = (end + 1) % len(lst)
    return total

def lists_with_product_equal_n(circular_list):
    products = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            prod = circular_product(circular_list, i, j)
            if prod == 53:
                products.append(circular_list[i:j + 1])
    return products