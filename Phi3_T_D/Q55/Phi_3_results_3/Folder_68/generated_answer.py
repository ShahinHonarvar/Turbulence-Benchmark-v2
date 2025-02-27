def circular_product_sublists(circular_list, target_product=6):
    size = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    result.sort()
    result = [result[i] for i in range(len(result)) if i == 0 or result[i] != result[i - 1]]
    return result

def lists_with_product_equal_n(circular_list):
    return circular_product_sublists(circular_list)