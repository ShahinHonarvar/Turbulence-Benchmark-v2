def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def find_sublists_with_product(start):
        product = 1
        for i in range(n):
            product *= circular_list[(start + i) % n]
            if product == -22:
                result.append(circular_list[start:start + i + 1])
    for i in range(n):
        find_sublists_with_product(i)
    return result