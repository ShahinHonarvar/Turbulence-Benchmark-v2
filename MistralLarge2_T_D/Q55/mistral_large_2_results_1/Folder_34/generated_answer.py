def lists_with_product_equal_n(circular_list):
    n, size = (-81, len(circular_list))
    result = []

    def generate_sublists(start):
        product = 1
        sublist = []
        for i in range(size):
            product *= circular_list[(start + i) % size]
            sublist.append(circular_list[(start + i) % size])
            if product == n:
                result.append(sublist[:])
            if product == 0:
                break
    for i in range(size):
        generate_sublists(i)
    return result