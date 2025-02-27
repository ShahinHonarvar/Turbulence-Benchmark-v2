def lists_with_product_equal_n(circular_list, target=18):
    circle_size = len(circular_list)
    results = []
    for i in range(circle_size):
        prod = 1
        sublist = []
        for j in range(i, i + circle_size):
            index = j % circle_size
            prod *= circular_list[index]
            sublist.append(circular_list[index])
            if prod == target:
                results.append(sublist.copy())
                break
            elif prod > target:
                prod = 1
                break
    return results