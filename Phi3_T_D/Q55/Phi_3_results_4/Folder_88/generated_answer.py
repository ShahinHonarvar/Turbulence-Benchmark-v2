def lists_with_product_equal_n(circular_list):
    target_product = 56
    n = len(circular_list)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist_product = 1
            sublist = []
            for i in range(size):
                index = (start + i) % n
                sublist.append(circular_list[index])
                sublist_product *= circular_list[index]
            if sublist_product == -target_product:
                negatives = sum((1 for x in sublist if x < 0))
                positives = sum((1 for x in sublist if x > 0))
                if negatives % 2 == 1 and positives >= 1 or (negatives % 2 == 0 and positives > 0):
                    result.append(sublist)
    return result