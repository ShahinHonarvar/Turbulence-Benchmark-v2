def lists_with_product_equal_n(circular_list):
    product = 0
    n = 15
    indices = []
    results = []

    def recurse(start, temp):
        nonlocal product
        if product == n:
            results.append(temp)
            return
        if product > n:
            return
        for i in range(start, len(circular_list) + start):
            product *= circular_list[i % len(circular_list)]
            temp.append(circular_list[i % len(circular_list)])
            recurse(i + 1, temp)
            temp.pop()
            product //= circular_list[i % len(circular_list)]
    recurse(0, [])
    return results