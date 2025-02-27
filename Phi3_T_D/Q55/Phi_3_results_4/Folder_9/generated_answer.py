def lists_with_product_equal_n(circle):

    def check_product(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circle[i % len(circle)]
        return product == -36
    result = []
    for size in range(1, len(circle) + 1):
        for i in range(len(circle)):
            sublist = circle[i:i + size]
            circle_head_tail = circle[len(sublist) - 1:] + circle[:len(sublist) - 1]
            if check_product(i, i + size - 1) and circle != circle_head_tail:
                results.append(sublist)
    return result