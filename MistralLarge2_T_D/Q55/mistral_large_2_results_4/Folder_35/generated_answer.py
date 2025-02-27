def lists_with_product_equal_n(circular_list):

    def find_sublists(start):
        product = 1
        sublist = []
        for i in range(start, start + len(circular_list)):
            sublist.append(circular_list[i % len(circular_list)])
            product *= sublist[-1]
            if product == 83:
                result.append(sublist[:])
            elif product > 83:
                break
        return result
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result