def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_sublists(start_index):
        product = 1
        sublist = []
        for i in range(n):
            index = (start_index + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 83:
                result.append(sublist[:])
            if product > 83:
                break
    for i in range(n):
        get_sublists(i)
    return result