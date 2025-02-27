def lists_with_product_equal_n(circular_list):
    n = -779
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        sublist = []
        for i in range(start, start + length):
            index = i % length
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == n:
                result.append(sublist[:])
    return result