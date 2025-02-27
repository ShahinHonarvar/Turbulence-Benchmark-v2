def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst, length):
        for i in range(len(lst)):
            yield [lst[(i + j) % len(lst)] for j in range(length)]
    n = -36
    result = []
    for size in range(1, len(circular_list) + 1):
        for sublist in circular_sublists(circular_list, size):
            if abs(sublist.count(0) - sublist.count(-1)) <= 1 and abs(sublist.count(0) - sublist.count(36)) <= 1:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result