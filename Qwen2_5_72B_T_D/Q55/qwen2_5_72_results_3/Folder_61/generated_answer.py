def lists_with_product_equal_n(arr):

    def find_sublists(index, product, current, all_results):
        if product == -10:
            all_results.append(current[:])
        if index >= len(arr):
            if product == -10 and current:
                all_results.append(current[:])
            return
        for i in range(len(arr)):
            if index + i >= len(arr):
                next_index = (index + i) % len(arr)
            else:
                next_index = index + i
            current.append(arr[next_index])
            find_sublists(next_index + 1, product * arr[next_index], current, all_results)
            current.pop()
    results = []
    find_sublists(0, 1, [], results)
    return results