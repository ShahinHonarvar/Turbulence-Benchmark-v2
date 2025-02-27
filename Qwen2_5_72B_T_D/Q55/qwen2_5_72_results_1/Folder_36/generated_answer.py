def lists_with_product_equal_n(circular_list):
    target_product = 714
    n = len(circular_list)
    results = []

    def find_sublists(start, product, sub_list):
        if product == target_product:
            results.append(sub_list.copy())
            return
        if product != 0 and product % target_product == 0 and (target_product % product == 0):
            return
        for i in range(n):
            index = (start + i) % n
            new_product = product * circular_list[index]
            sub_list.append(circular_list[index])
            find_sublists((start + i + 1) % n, new_product, sub_list)
            sub_list.pop()
    for i in range(n):
        find_sublists(i, 1, [])
    return results