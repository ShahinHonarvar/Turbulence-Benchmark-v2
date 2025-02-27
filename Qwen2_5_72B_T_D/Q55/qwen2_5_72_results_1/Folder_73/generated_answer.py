def lists_with_product_equal_n(circular_list):
    target_product = 40
    n = len(circular_list)
    result = []

    def find_sublists(start, temp_list, product):
        if product == target_product:
            result.append(temp_list)
            return
        if product > target_product:
            return
        for i in range(n):
            new_start = (start + i) % n
            new_product = product * circular_list[new_start]
            find_sublists(new_start + 1, temp_list + [circular_list[new_start]], new_product)
    for i in range(n):
        find_sublists(i, [], 1)
    final_result = [sublist for sublist in result if len(sublist) <= n]
    return final_result