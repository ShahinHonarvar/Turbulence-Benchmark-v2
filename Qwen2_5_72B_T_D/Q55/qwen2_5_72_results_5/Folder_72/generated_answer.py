def lists_with_product_equal_n(circular_list):

    def find_sublists(start, n):
        product, sublists, length = (1, [], len(circular_list))
        for size in range(1, length + 1):
            for i in range(size):
                index = (start + i) % length
                product *= circular_list[index]
            if product == n:
                sublists.append(circular_list[start:start + size] if start + size <= length else circular_list[start:] + circular_list[:size - (length - start)])
            product //= circular_list[(start + size - 1) % length]
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(find_sublists(i, 10))
    return result