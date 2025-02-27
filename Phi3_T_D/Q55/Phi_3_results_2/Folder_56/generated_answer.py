def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_n(start, end, subset, total_product):
        product = 1
        while start != end and product / total_product <= 65:
            product *= circular_list[start % len(circular_list)]
            subset.append(circular_list[start % len(circular_list)])
            if product == -65:
                results.append(subset.copy())
            find_sublists_with_product_n(start + 1, end, subset, total_product)
            subset.pop()
            if product != 0:
                product //= circular_list[start % len(circular_list)]
            start += 1
    results = []
    for i in range(len(circular_list)):
        find_sublists_with_product_n(i, i, [], 1)
    return results