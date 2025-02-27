def lists_with_product_equal_n(circular_list):

    def find_sublists_product_n(start, product, n, current, result):
        if start >= len(circular_list):
            return
        if product * circular_list[start % len(circular_list)] == n:
            result.append(current + [circular_list[start % len(circular_list)]])
        if start < len(circular_list):
            for i in range(start, len(circular_list) + start):
                new_product = product * circular_list[i % len(circular_list)]
                if new_product == n:
                    result.append(current + [circular_list[i % len(circular_list)]])
                if new_product != 0:
                    find_sublists_product_n(i + 1, new_product, n, current + [circular_list[i % len(circular_list)]], result)
    all_results = []
    for i in range(len(circular_list)):
        find_sublists_product_n(i, 1, -20, [], all_results)
    return all_results