def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, n):
        sublists = []
        current_product = 1
        for i in range(n):
            index = (start + i) % n
            current_product *= circular_list[index]
            if current_product == product:
                sublists.append(circular_list[start:index + 1])
            elif current_product > product:
                break
        return sublists
    result = []
    n = len(circular_list)
    for start in range(n):
        result.extend(find_sublists(start, 25, n))
    return result