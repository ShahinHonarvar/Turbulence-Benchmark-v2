def lists_with_product_equal_n(lst):

    def find_sublists(start):
        product = 1
        result = []
        for end in range(start, len(lst) + start):
            product *= lst[end % len(lst)]
            if product == 33:
                result.append(lst[start % len(lst):(end + 1) % len(lst)] if end + 1 < start + len(lst) else lst[start:] + lst[:(end + 1) % len(lst)])
            elif product > 33:
                break
        return result
    all_results = [find_sublists(i) for i in range(len(lst))]
    flat_results = [item for sublist in all_results for item in sublist]
    return flat_results