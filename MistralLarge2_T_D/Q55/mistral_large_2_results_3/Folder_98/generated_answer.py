def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []

    def find_sublists(start):
        product = 1
        for i in range(n):
            product *= circular_list[(start + i) % n]
            if product == -1:
                results.append(circular_list[start:start + i + 1])
    for i in range(n):
        find_sublists(i)
    return results