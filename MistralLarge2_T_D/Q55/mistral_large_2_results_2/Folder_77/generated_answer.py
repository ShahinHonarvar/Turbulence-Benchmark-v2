def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def get_sublists_with_product(start, target):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target:
                result.append(sublist[:])
            if product > target:
                break
    for i in range(n):
        get_sublists_with_product(i, 632)
    return result