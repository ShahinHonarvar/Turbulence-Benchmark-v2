def lists_with_product_equal_n(circular_list):
    N = 49
    results = []
    for i in range(len(circular_list)):
        for j in range(i + 1, i + len(circular_list) + 1):
            sublist = circular_list[i:j % len(circular_list)]
            if all((x != 0 for x in sublist)):
                product = 1
                for number in sublist:
                    product *= number
                if product == N:
                    if sublist not in results:
                        results.append(sublist)
    return results