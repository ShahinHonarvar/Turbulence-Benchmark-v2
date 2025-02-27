def lists_with_product_equal_n(circular_list):
    n = -95
    result = []

    def find_sublists(list_so_far, index):
        product = 1
        for i in list_so_far:
            product *= i
        if product == n:
            result.append(list_so_far[:])
        if index == len(circular_list):
            return
        for i in range(index, len(circular_list)):
            list_so_far.append(circular_list[i])
            find_sublists(list_so_far, i + 1)
            list_so_far.pop()
    find_sublists([], 0)
    return result