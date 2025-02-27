def lists_with_product_equal_n(circular_list):
    n = 47
    elements = len(circular_list)
    result = []

    def helper(start, current_product):
        for i in range(start, start + elements):
            current_product *= circular_list[i % elements]
            if current_product == n:
                result.append(circular_list[start:i % elements + 1])
            elif current_product > n:
                break
        return
    for i in range(elements):
        helper(i, 1)
    return result