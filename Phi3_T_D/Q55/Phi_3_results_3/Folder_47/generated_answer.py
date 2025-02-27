def lists_with_product_equal_n(circular_list):
    n = -94
    sublists = []

    def find_sublists(start, product=1):
        for i in range(start, len(circular_list) + start):
            idx = i % len(circular_list)
            product *= circular_list[idx]
            if product == n:
                sublists.append(circular_list[start:i + 1 if i != start else i])
            if product > n:
                break
    for i in range(len(circular_list)):
        find_sublists(i)
        for _ in range(len(circular_list) - 1):
            circular_list.append(circular_list.pop(0))
            find_sublists(i)
    return sublists