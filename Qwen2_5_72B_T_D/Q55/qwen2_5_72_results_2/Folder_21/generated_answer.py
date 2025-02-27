def lists_with_product_equal_n(circular_list):
    target_product = 851
    n = len(circular_list)
    result = []

    def find_sublists(start, product, sublist):
        if product == target_product:
            result.append(sublist.copy())
        if product != 0 and product % target_product == 0:
            return
        for i in range(n):
            index = (start + i) % n
            if index == start and len(sublist) > 0:
                break
            find_sublists(start, product * circular_list[index], sublist + [circular_list[index]])
    for i in range(n):
        find_sublists(i, 1, [])
    return result