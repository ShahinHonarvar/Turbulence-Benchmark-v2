def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == 714:
                sublist = circular_list[start:start + end + 1]
                if start + end + 1 > n:
                    sublist += circular_list[:(start + end + 1) % n]
                result.append(sublist)
            elif product > 714:
                break
    return result