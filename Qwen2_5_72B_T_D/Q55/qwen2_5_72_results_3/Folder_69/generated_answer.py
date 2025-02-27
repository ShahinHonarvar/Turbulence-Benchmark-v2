def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product, current):
        if product == 90:
            results.append(current[:])
            return
        for i in range(len(circular_list)):
            index = (start + i) % len(circular_list)
            item = circular_list[index]
            if product * item <= 90:
                current.append(item)
                find_sublists(index + 1, product * item, current)
                current.pop()
            else:
                break
    results = []
    find_sublists(0, 1, [])
    return results