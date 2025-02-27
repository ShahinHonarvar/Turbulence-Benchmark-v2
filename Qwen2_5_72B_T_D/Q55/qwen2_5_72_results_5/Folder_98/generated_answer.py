def lists_with_product_equal_n(circular_list):

    def find_sublists(start, length):
        sublists = []
        current_product = 1
        for i in range(length):
            current_product *= circular_list[(start + i) % length]
        for end in range(start, start + length):
            if current_product == -1:
                sublists.append(circular_list[start:end + 1])
            current_product //= circular_list[(end - start) % length]
            if end < start + length - 1:
                current_product *= circular_list[(end + 1) % length]
        return sublists
    size = len(circular_list)
    result = []
    for i in range(size):
        result.extend(find_sublists(i, size))
    return result