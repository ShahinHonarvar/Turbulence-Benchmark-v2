def lists_with_product_equal_n(circular_list):

    def find_sublists(start):
        product = 1
        for length in range(1, len(circular_list) + 1):
            product *= circular_list[(start + length - 1) % len(circular_list)]
            if product == -36:
                result.append(circular_list[start:start + length])
            elif product > 36:
                break
    result = []
    for i in range(len(circular_list)):
        find_sublists(i)
    return result