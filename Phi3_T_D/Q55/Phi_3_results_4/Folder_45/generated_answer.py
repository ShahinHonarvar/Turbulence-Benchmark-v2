def lists_with_product_equal_n(circular_list, target=-5):
    n = len(circular_list)
    if n == 0:
        return []
    product_lists = []

    def search_sublists(index, current_list):
        product = 1
        for num in current_list:
            product *= num
        if product == target:
            product_lists.append(current_list)
        for i in range(index + 1, n):
            new_list = current_list + [circular_list[i]]
            search_sublists(i, new_list)
        new_list = circular_list[-(n - index - 1):] + current_list
        search_sublists(0, new_list)
    search_sublists(0, [])
    return product_lists