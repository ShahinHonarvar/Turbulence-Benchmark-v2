def lists_with_product_equal_n(circular_list):

    def find_sublists(start):
        product, sublist = (1, [])
        for i in range(len(circular_list)):
            idx = (start + i) % len(circular_list)
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 100:
                result.append(sublist[:])
            elif product > 100 or product == 0:
                break
        return
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result if result else []