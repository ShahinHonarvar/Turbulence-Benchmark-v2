def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def find_sublists(start):
        product = 1
        for i in range(n):
            product *= circular_list[(start + i) % n]
            if product == 53:
                result.append(circular_list[start:start + i + 1])
            elif product > 53 or (i > 0 and product == 0):
                break
    for i in range(n):
        find_sublists(i)
    return result