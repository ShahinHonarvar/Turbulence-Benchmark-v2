def lists_with_product_equal_n(circular_list, n=76):
    circular_list = circular_list + circular_list[0:1]
    result = []
    for start in range(len(circular_list) - 1):
        for end in range(start + 1, len(circular_list)):
            sublist = circular_list[start:end]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                result.append(sublist)
    return result