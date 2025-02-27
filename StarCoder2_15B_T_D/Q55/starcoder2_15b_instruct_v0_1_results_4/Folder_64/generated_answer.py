def lists_with_product_equal_n(circular_list):
    sublists = []
    n = 3
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and len(sublist) > 0:
                product = 1
                for k in sublist:
                    product *= k
                if product == n:
                    sublists.append(sublist)
    return sublists