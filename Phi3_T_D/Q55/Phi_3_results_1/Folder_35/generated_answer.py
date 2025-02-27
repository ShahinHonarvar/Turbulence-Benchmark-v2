def lists_with_product_equal_n(lst, product=83):
    n = len(lst)
    result = []

    def inner(index, current_product, current_list):
        if current_product == product and len(current_list) > 1:
            result.append(current_list)
            return
        if current_product > product or index == n:
            return
        for i in range(index, n + index):
            number = lst[i % n]
            if not current_list or number != current_list[-1]:
                inner(i + 1, current_product * number, current_list + [number])
    inner(0, 1, [])
    return result