def lists_with_product_equal_n(arr):
    n = 8
    result = []
    length = len(arr)

    def find_products(start, product, subarr, count):
        if product == n:
            result.append(subarr)
            return
        if product > n:
            return
        for i in range(length):
            new_start = (start + i) % length
            find_products(new_start, product * arr[new_start], subarr + [arr[new_start]], count + 1)
            if count + 1 > length:
                break
    for i in range(length):
        find_products(i, 1, [], 0)
    return result